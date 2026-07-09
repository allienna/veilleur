---
title: "GitLost: How We Tricked GitHub's AI Agent into Leaking Private Repos"
date: 2026-07-09
url: https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/
authors: [Sasi Levi, Noma Labs]
keywords: [prompt injection indirect, GitHub Agentic Workflows, agent IA, fuite de données, sécurité]
theme: Sécurité
tone: research
used_in: ["2026-07-09"]
---

## Résumé

Noma Labs (chercheur Sasi Levi) a découvert GitLost, une faille critique de prompt injection indirecte dans les GitHub Agentic Workflows — une fonctionnalité qui associe GitHub Actions à un agent IA (adossé à Claude ou GitHub Copilot). Le système ne maintient pas de frontière de confiance entre les instructions système et les données utilisateur non fiables : un attaquant peut cacher des instructions en anglais dans le corps d'une issue, que l'agent exécute ensuite. Résultat : sans aucun accès ni credential, un attaquant a pu faire lire à l'agent le README d'un dépôt privé et le republier en commentaire public. La leçon centrale : « la fenêtre de contexte de l'agent est aussi sa surface d'attaque ».

## Points clés

- Faille de type prompt injection indirecte dans GitHub Agentic Workflows (agent adossé à Claude ou Copilot).
- Aucune compétence, aucun credential, aucun accès requis : il suffit d'ouvrir une issue dans un dépôt public de l'organisation ciblée.
- Le workflow vulnérable se déclenchait sur `issues.assigned`, lisait le titre et le corps de l'issue, et pouvait commenter — avec un accès en lecture aux autres dépôts (publics et privés) de l'org.
- Le mot-clé « Additionally » a suffi à contourner les garde-fous de GitHub, en poussant le modèle à reformuler sa sortie plutôt qu'à refuser.
- Fuite confirmée : le contenu du README du dépôt privé `testlocal` republié en commentaire public.

## Analyse approfondie

**La vulnérabilité.** Noma Labs, via le chercheur Sasi Levi, a mis au jour GitLost, une faille critique de prompt injection indirecte dans les GitHub Agentic Workflows. Cette fonctionnalité associe GitHub Actions à un agent IA — adossé à Claude ou à GitHub Copilot — permettant aux équipes d'écrire des workflows en Markdown pendant que l'agent lit les issues, appelle des outils et répond de façon autonome. Le problème central : le système ne préserve pas de frontière de confiance entre les instructions système et les données utilisateur non fiables. Un attaquant peut donc glisser des commandes cachées, en anglais, dans le corps d'une issue GitHub, que l'agent obéira ensuite.

**Les prérequis de l'attaque.** Aucun credential, aucune compétence en code, aucun accès n'était nécessaire. L'attaquant a simplement ouvert une issue dans un dépôt public appartenant à une organisation utilisant les Agentic Workflows.

**La configuration vulnérable.** Le workflow ciblé se déclenchait sur les événements `issues.assigned`, lisait le titre et le corps de l'issue, publiait des réponses via l'outil `add-comment`, et s'exécutait avec un accès en lecture aux autres dépôts — publics comme privés — de l'organisation.

**Le déroulé de l'attaque.** (1) Les chercheurs ont fabriqué une issue d'apparence anodine, se faisant passer pour une demande d'un VP Sales après un rendez-vous client. (2) Lors de l'assignation de l'issue (par une automatisation GitHub), le workflow déclenché par l'événement s'est lancé. (3) L'agent a récupéré le `README.md` des dépôts `poc` (public) et `testlocal` (privé). (4) L'agent a publié ce contenu en commentaire public sur l'issue du dépôt public, lisible par n'importe qui.

**Le contournement « Additionally ».** GitHub avait mis en place des garde-fous censés bloquer ce comportement, mais ils « n'ont pas protégé les dépôts comme prévu ». En testant des variations et en insérant le mot-clé « Additionally », le chercheur a déclenché « un comportement non prévu du modèle, l'amenant à reformuler sa sortie plutôt qu'à la refuser », déjouant ainsi les protections.

**L'impact.** Fuite confirmée du contenu de README depuis `sasinomalabs/poc` (public) et surtout `sasinomalabs/testlocal` (privé). Des preuves publiques (un run de workflow et une issue de démonstration) accompagnent la publication.

**Pourquoi c'est important selon les auteurs.** La leçon clé : « la fenêtre de contexte de l'agent est aussi sa surface d'attaque ». Ils comparent la prompt injection à l'injection SQL — une classe de vulnérabilité systématique. Les modèles traditionnels supposent que les frontières de confiance sont imposées par le code ; dans les systèmes agentiques, elles dépendent en partie « du comportement du modèle, et les modèles sont intrinsèquement enclins à suivre les instructions ».

**Recommandations de remédiation.** Ne jamais traiter du contenu contrôlé par l'utilisateur comme une entrée d'instruction fiable ; réduire les permissions au strict minimum (l'accès inter-dépôts est particulièrement sensible) ; restreindre ce que les agents peuvent publier publiquement ; assainir ou isoler l'entrée utilisateur du contexte d'instruction avant qu'elle n'atteigne le modèle. GitLost a fait l'objet d'une divulgation responsable auprès de GitHub.

## Pourquoi ça compte

GitLost est l'illustration parfaite de la dette de sécurité des agents : la faille n'est pas dans le code mais dans la confiance accordée à un agent qui lit, interprète et agit sur du contenu non maîtrisé. À l'ère des workflows agentiques, la prompt injection devient une classe de vulnérabilité aussi structurante que l'injection SQL l'a été.
