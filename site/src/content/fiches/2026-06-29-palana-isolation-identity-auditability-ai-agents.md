---
title: "Palana (Part 2): Architecting isolation, identity, and auditability for AI agents"
date: 2026-06-29
url: https://substack.com/redirect/cd43f8b4-f65b-4e63-9367-38372ac985ae?j=eyJ1IjoiN3Y1bG1jIn0.HlvPOGYPdVknSYzEK1JIj6IFkAFn8zuyjtfU9Mbft9Q
authors: [Grab Engineering]
keywords: [Kubernetes, Vault, network policy, identité, audit, agents IA]
theme: IA
tone: news
used_in: ["2026-06-29"]
---

## Résumé

Deuxième partie de la série Palana de Grab : l'architecture concrète qui rend les agents IA isolés, identifiables et auditables. Chaque agent tourne dans un namespace dédié, avec une network policy default-deny, des credentials lus uniquement par le composant autorisé via Vault, et une egress forcée à travers des proxys. L'identité brute de l'utilisateur est conservée comme propriétaire faisant autorité, distincte des formes « sanitized » utilisées pour nommer les objets Kubernetes. Tout le trafic — LLM, HTTP, Git — passe par des couches médiatrices qui le rendent attribuable.

## Points clés

- Le chemin de requête : un pod d'agent dans un namespace par utilisateur/agent, avec network policy default-deny, accès DNS, et volume persistant `/data`.
- L'opérateur transforme une requête utilisateur en objets Kubernetes concrets : namespaces, service accounts, role bindings, stockage, network policies, ingress.
- Identité : l'identité brute (email) reste l'autorité pour le matching RBAC ; les formes sanitized servent uniquement aux noms d'objets, labels et chemins Vault.
- Secrets : layout Vault à moindre privilège, avec un chemin lisible par l'agent et un chemin « proxy-only » où l'agent ne voit qu'un placeholder inerte.
- Réseau : Layer 3/4 via NetworkPolicy/Cilium, Layer 7 via politiques de proxy évaluées par OPA selon l'hôte, la méthode et l'identité de l'agent.

## Analyse approfondie

### Vue d'ensemble de l'architecture

Le chemin de requête central est le suivant. Le pod de l'agent tourne dans un namespace détenu par un seul utilisateur et un seul agent. Il reçoit une network policy de type default-deny, un accès DNS, l'accès aux services plateforme requis et un volume persistant `/data`. Le trafic navigateur entre via Traefik. Le trafic LLM passe par le wrapper LiteLLM dans le namespace gateway. L'egress HTTP/HTTPS générale passe par le namespace proxy. Les secrets ne sont lus dans Vault que par le composant autorisé à les utiliser.

L'opérateur est responsable de transformer une requête utilisateur en forme Kubernetes concrète :

1. L'utilisateur crée un agent via `pcli` (Palana command-line interface) ou le portail.
2. Palana écrit une custom resource UserAgent ou Agent avec l'identité utilisateur brute.
3. L'opérateur crée les namespaces utilisateur et agent, les service accounts, role bindings, le stockage, les network policies et l'ingress.
4. L'utilisateur lance un template ou une image de conteneur.
5. Des admission webhooks injectent les variables d'environnement du proxy et imposent les restrictions au niveau du pod.
6. Les logs, décisions de politique et signaux d'activité sont émis vers les systèmes d'observabilité.

### Cycle de vie d'un agent

Du point de vue de l'utilisateur, le workflow de base est volontairement réduit :

```
./pcli login
./pcli create demo
./pcli secrets add demo GRABGPT_API_KEY token=<token>
./pcli run demo --template claudecodeui
```

Derrière ces commandes, Palana provisionne un environnement d'exécution isolé :

- Namespace : `agent-{sanitized-user}-{agent}`
- Service account : lié uniquement à ce namespace
- Stockage : un PVC adossé à Amazon EFS, monté sur `/data`
- Ingress : un hostname spécifique à l'agent, protégé par une auth navigateur adossée à Concedo
- Egress : forcée à travers les proxys de la plateforme, sauf pour les services internes approuvés
- Secrets : répartis entre chemins Vault lisibles par l'agent et chemins proxy-only
- Policies : egress proxy, egress réseau, et règles optionnelles de peering inter-agents

### Comment Palana gère l'identité

L'authentification humaine utilise Concedo en OpenID Connect (OIDC). `pcli login` exécute un flux d'autorisation par navigateur avec PKCE et stocke l'identité résultante dans un kubeconfig isolé. L'accès navigateur aux UI des agents est protégé par OAuth2-Proxy via le forward auth de Traefik.

Détail important : Palana conserve l'identité utilisateur brute, l'adresse email, comme propriétaire faisant autorité sur la custom resource. Cette identité brute sert de sujet pour le matching RBAC de Kubernetes. Les formes sanitized ne servent que là où les noms d'objets, labels, namespaces ou chemins Vault exigent des chaînes plus sûres. Cette séparation prévient une classe courante de bugs d'identité : la version « affichable » ou « path-safe » d'un identifiant utilisateur ne doit jamais devenir accidentellement le sujet d'autorisation. À terme, Grab prévoit d'intégrer Palana via SPIFFE/SPIRE dans son service mesh, pour fournir une identité agentique — combinaison de l'utilisateur et de l'instance d'agent — dotée d'un sous-ensemble contrôlé des capacités de l'utilisateur.

### Comment Palana gère les secrets

Le layout Vault est conçu autour du moindre privilège :

```
kv/agents/{user}/{agent}/{secret}
kv/proxy-secrets/{user}/{agent}/{secret}
```

Le premier chemin contient les secrets que l'agent est autorisé à lire via son rôle Vault par agent. Le second contient les credentials que l'agent ne peut utiliser qu'à travers le proxy. Pour chaque secret proxy-only, Palana crée une valeur placeholder visible par l'agent — inerte tant que la requête ne passe pas par le chemin proxy approuvé. Cela donne un chemin de migration pratique : les clients existants peuvent souvent être configurés avec une valeur ressemblant à un token, tandis que Palana garde le vrai token hors du runtime.

### Comment Palana gère l'accès LLM

Les appels LLM passent par `litellm-proxy-wrapper`, placé devant LiteLLM et GrabGPT. Le wrapper dérive l'identité de l'agent depuis le contexte Kubernetes plutôt que de faire confiance aux headers fournis par le client, puis récupère le credential GrabGPT par agent dans Vault et forwarde la requête vers la bonne route upstream. Cela offre trois propriétés utiles : les agents n'ont pas besoin des credentials LLM bruts, le trafic LLM est attribuable à un agent précis, et le routage providers/credentials peut évoluer de façon centralisée.

### Comment Palana gère l'accès réseau

Le contrôle réseau est découpé en deux couches. En Layer 3/4, Kubernetes NetworkPolicy et Cilium imposent à quels namespaces, services et blocs CIDR les pods peuvent parler. Les namespaces d'agents sont verrouillés sur les seuls chemins plateforme nécessaires : DNS, Vault, proxy d'egress, gateway LLM, et les patterns d'API Kubernetes explicitement supportés. En Layer 7, la politique de proxy contrôle les destinations HTTP/HTTPS par hôte, méthode et identité d'agent. Open Policy Agent (OPA) évalue les politiques par agent.

## Pourquoi ça compte

C'est le plan détaillé, réutilisable, de ce que signifie « traiter un agent IA comme un workload de première classe » : isolation comme unité de confiance, credentials hors de portée, et tout le trafic médiatisé et attribuable. Une référence concrète pour quiconque met des agents en production.
