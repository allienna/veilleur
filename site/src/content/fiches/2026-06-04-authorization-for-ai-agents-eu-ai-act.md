---
title: "Authorization for AI agents: What to build before the EU AI Act deadline"
date: 2026-06-04
url: https://cerbos.dev/blog/authorization-for-ai-agents-what-to-build-before-eu-ai-act-deadline
authors: [Cerbos]
keywords: [autorisation agents, identité non-humaine, audit délégation, fail-closed, EU AI Act]
theme: Tech
tone: opinion
used_in: ["2026-06-04"]
---

## Résumé

Cerbos part d'une phrase de Jonathan Care (KuppingerCole) : « les frameworks gouvernent ce que les modèles *disent* ; presque rien ne gouverne ce que les agents *font* ». L'auteur découpe ce trou en trois couches : l'identité (par instance d'agent, à durée de vie liée à un sponsor humain), l'audit (qui survit aux délégations entre sous-agents), et l'orchestration (le gating des appels d'outils hors de l'agent, avec un runtime fail-closed). Les deux premières sont familières à l'industrie IAM ; la troisième n'a pas encore de catégorie mature. L'EU AI Act donne l'urgence, mais l'obligation architecturale demeure quelle que soit la date : sortir la politique de décision de l'agent lui-même.

## Points clés

- La phrase-clé : les frameworks gouvernent ce que les modèles disent, presque rien ne gouverne ce que les agents font.
- Trois couches : identité par instance (pas par classe), audit survivant à la délégation, orchestration (gating d'outils hors agent, fail-closed).
- Aujourd'hui : une clé API longue durée par « l'agent », chaque instance traitée comme le même acteur — casse dès qu'un agent en spawn un autre.
- Le moteur de politique doit être externalisé (pattern PEP/PDP), décidant *avant* l'appel d'outil — l'agent ne décide plus de ce qu'il peut faire (« la sécurité de l'inmate écrite par l'inmate »).
- EU AI Act (articles 9, 10, 12, 13) : obligations sur le *fournisseur* du système IA, pas sur les vendeurs d'infra ; activation Annex III initialement août 2026, possiblement repoussée à décembre 2027.
- À faire ce trimestre : inventorier les agents (shadow AI), sponsoriser chaque agent (si Sally part, ses agents s'arrêtent), sortir la politique de l'agent, câbler la chaîne d'audit, tester le comportement fail-closed.
- Signal à surveiller chez les vendeurs : la politique est-elle découplée de l'agent ? Sinon, c'est autre chose.

## Analyse approfondie

L'auteur ouvre sur une phrase de Jonathan Care (KuppingerCole) qui le hante : « Frameworks govern what models say. Almost nothing governs what agents do. » C'est le trou. Les équipes qu'il rencontre y arrivent par des angles différents — le CTO veut des agents en prod et la sécurité refuse de signer ; le juridique s'inquiète de l'EU AI Act — mais c'est le même manque dessous.

**Trois trous, un seul nommé.** Trois couches, chacune avec un acronyme émergent, mais la forme compte plus que l'acronyme :

1. *Identité.* Chaque agent a besoin de sa propre identité, par instance et non par classe : credentials à courte durée scopés à un seul appel d'outil, cycle de vie lié à un sponsor humain nommé. Aujourd'hui la plupart des entreprises émettent une clé API longue durée par « l'agent » et traitent chaque instance spawnée comme le même acteur — ce qui cesse de fonctionner dès qu'un agent en spawn un autre (cf. non-human identity et sponsor-tied lifecycle).

2. *Audit.* Dès qu'un agent délègue à un sous-agent, toute piste d'audit existante se brise. Qui a consenti ? Quel était le but initial ? Le consentement a-t-il survécu au saut ? Les logs d'aujourd'hui ne répondent à rien de tout cela : ils disent qu'un compte de service a fait quelque chose, pas quel humain l'a autorisé, par quelle chaîne, dans quel but, sur quelles données. La chaîne de responsabilité (chain of custody) est la pièce manquante, et un enjeu plus grand qu'on ne le reconnaît.

3. *Orchestration.* La couche sans catégorie mature : agent-à-agent et agent-à-outil. Gating des outils *hors* de l'agent, application de la confiance inter-agents, runtime fail-closed quand le plan de politique est injoignable. Aujourd'hui cette couche n'est que ce que le framework d'agent a choisi d'exposer — souvent l'agent lui-même décide quels outils il peut appeler, ce qui revient à « demander à un enfant s'il a le droit de prendre un dessert ». Les deux premières couches sont des problèmes que l'IAM sait penser ; la troisième n'a été nommée par personne comme catégorie propre. Pour l'auteur, la nommer est le moment où elle devient réelle.

**Ce que « politique runtime à la couche d'orchestration » veut dire.** Chaque appel agent-à-outil est une décision : cet agent, agissant pour le compte de cet humain, dans ce contexte, doit-il pouvoir invoquer cet outil avec ces arguments ? L'agent ne doit pas être celui qui décide. Un moteur de politique séparé doit le faire, hors de la boucle de raisonnement de l'agent, évaluant l'appel avant qu'il ne passe. C'est le même pattern d'autorisation externalisée (PEP/PDP, PBAC) qu'en application classique, avec l'agent comme nouveau type de *principal* et l'outil comme nouveau type de *ressource* — découplé, externalisé, fail-closed si le moteur est injoignable. Sans cela, tous les autres contrôles vivent *à l'intérieur* de l'agent (guardrails de prompt, allowlists du framework, system prompts « n'appelle pas l'outil de remboursement ») — soit « des contrôles sur l'inmate, écrits par l'inmate ». Sortir la politique de l'agent donne ce qu'une équipe sécurité peut raisonner : même moteur sur tous les agents, même log d'audit, même change management, même rollback.

**La deadline d'août, et pourquoi c'est la plus petite histoire.** L'urgence vient de l'EU AI Act : l'article 9 (gestion du risque), 10 (gouvernance des données), 12 (enregistrement automatique sur la durée de vie), 13 (transparence aux déployeurs) forment le cœur opérationnel de ce qu'un système IA à haut risque doit démontrer. Ces obligations pèsent sur le *fournisseur* du système IA, pas sur Cerbos ni aucun vendeur d'infra — l'auteur insiste : Cerbos ne satisfait pas l'article 9 à votre place, ne vous rend pas « conforme AI Act » ; quiconque l'affirme vend une histoire. Ce que Cerbos aide à faire, c'est la partie quasi impossible à démontrer sans contrôles runtime à sa couche : un process de gestion du risque qui n'applique pas de décisions à la frontière agent-outil n'est qu'un document ; une gouvernance des données qui ne filtre pas ce qu'un agent peut lire n'est pas une gouvernance ; un log automatique qui manque les décisions d'autorisation runtime n'est pas une chaîne de responsabilité. Côté calendrier : l'activation des obligations haut risque (Annex III) était initialement fixée à août 2026 ; la proposition Digital Omnibus de la Commission (novembre 2025) a poussé un report à décembre 2027, accord provisoire Conseil/Parlement début mai. La date peut glisser ; l'obligation architecturale, non.

**Pourquoi ça converge maintenant.** Vendeurs, analystes et utilisateurs finaux atterrissent sur la même forme architecturale depuis des points de départ différents : identité scopée par agent à cycle lié au sponsor, chaînes d'audit survivant à la délégation, plan de politique runtime gatant les appels d'outils hors agent. La checklist en huit questions de Care, le framework « tectonic-shifts » de Martin Kuppinger, la référence agentic IAM de CoSAI, et AuthZEN (que l'auteur co-préside à l'OpenID Foundation) couvrent le même terrain. Quand autant de fils indépendants convergent, la catégorie est nommée ; les implémentations doivent rattraper.

**Ce que les responsables sécurité doivent faire ce trimestre.** Dans l'ordre : (1) *Inventorier* — la plupart des organisations nient le nombre d'agents qu'elles ont déjà (trois équipes en ont pendant que la direction dit que non) ; traiter le shadow AI comme le shadow IT, mais plus rapide. (2) *Sponsoriser chaque agent* — un propriétaire humain nommé dont le statut de cycle de vie conditionne l'existence de l'agent ; si Sally part, les agents de Sally s'arrêtent (changement autant de gouvernance que technique). (3) *Sortir la politique de l'agent* — choisir un moteur de politique runtime évaluant les appels agent-à-outil de l'extérieur. (4) *Câbler la chaîne d'audit* — chaque action doit porter le sponsor humain, le but initial et la décision de politique, jusqu'à l'appel d'outil feuille (sinon impossible de répondre à la question d'explicabilité de l'article 86). (5) *Tester le fail-closed* — si le moteur de politique est injoignable et que « l'agent le fait quand même », vous avez un runtime qui fail-open : le pire bug de cette couche.

**Où ça va.** Les douze prochains mois seront bruyants : chaque vendeur d'infra revendiquera une « story runtime », certains re-skinnant du PAM ou de l'API gateway, quelques-uns réellement neufs. Le signal à surveiller : la politique est-elle découplée de l'agent ? Si elle vit encore dans l'agent, c'est autre chose. L'auteur préfère qu'on obtienne la bonne architecture plutôt que quiconque (Cerbos compris) ne revendique la conformité AI Act sur une slide. La deadline est une fonction de forçage ; le vrai travail est le runtime.

## Pourquoi ça compte

Nomme et structure le chaînon manquant de la sécurité agentique — l'autorisation runtime des appels d'outils, hors de l'agent — et donne une checklist actionnable avant l'échéance de l'EU AI Act. Le pendant « gouvernance/autorisation » du containment décrit par Anthropic.
