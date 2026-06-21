---
title: "Claude Code - Overview - Z.AI DEVELOPER DOCUMENT"
date: 2026-06-20
url: https://docs.z.ai/devpack/tool/claude
authors: [Z.ai, BigModel]
keywords: [Claude Code, GLM-5.2, reasoning effort, plan coding, MCP]
theme: IA
tone: tutorial
used_in: ["2026-06-20"]
---

## Résumé

Documentation développeur de Z.ai expliquant comment brancher le modèle chinois GLM-5.2 dans Claude Code. Elle détaille l'installation de Claude Code, la configuration du plan coding GLM, et le mapping des niveaux de « reasoning effort » de Claude Code vers ceux de GLM-5.2. L'enjeu : utiliser le harnais Claude Code avec un modèle alternatif bien moins cher, sans contournement maison.

## Points clés

- Claude Code est un outil de coding agentique vivant dans le terminal, qui comprend le codebase et automatise les tâches de routine, l'explication de code et les workflows git en langage naturel.
- Installation recommandée via npm (`npm install -g @anthropic-ai/claude-code`), prérequis Node.js 18+ (nvm conseillé sur macOS, Git for Windows sur Windows).
- Z.ai fournit un endpoint dédié : GLM-5.2 se branche dans Claude Code via un simple changement de configuration (plan coding payant).
- Mapping du reasoning effort : `low`/`medium`/`high` → `high` effectif côté GLM-5.2 ; `xhigh`/`max`/`ultracode` → `max`. Recommandation : `max` pour les tâches de code complexes.
- Commandes utiles : `/effort` pour changer le niveau de raisonnement, `/status` pour vérifier le modèle actif.

## Analyse approfondie

Claude Code est un outil de coding agentique qui vit dans votre terminal, comprend votre codebase et vous aide à coder plus vite en exécutant des tâches de routine, en expliquant du code complexe et en gérant les workflows git — le tout via des commandes en langage naturel.

**Étape 1 : Installer Claude Code.** Deux méthodes : installation recommandée, ou installation guidée par Cursor. Prérequis : Node.js 18 ou plus récent ; sur macOS, utiliser nvm pour installer Node.js (l'installation directe du package peut provoquer des problèmes de permissions) ; sur Windows, installer en plus Git for Windows. Commandes :

```
# Installer Claude Code
npm install -g @anthropic-ai/claude-code

# Aller dans votre projet
cd your-awesome-project

# Terminé
claude
```

Si vous n'êtes pas à l'aise avec npm mais avez Cursor, vous pouvez saisir la commande dans Cursor, qui vous guidera dans l'installation de Claude Code en lui demandant : « https://docs.anthropic.com/en/docs/claude-code/overview Help me install Claude Code ».

**Étape 2 : Configurer le plan coding GLM.** (Étapes 1 et 2 illustrées dans la doc d'origine.)

**Étape 3 : Démarrer avec Claude Code.** Une fois la configuration faite, on lance Claude Code dans le terminal :

```
cd your-project-directory
claude
```

Si l'invite « Do you want to use this API key » apparaît, sélectionner « Yes ». Après le lancement, accorder à Claude Code la permission d'accéder aux fichiers du dossier.

**Changer le reasoning effort.** Dans une session Claude Code, entrer `/effort` pour changer l'effort de raisonnement. Après le changement, Claude Code mappe le niveau sélectionné vers l'effort effectif utilisé par GLM-5.2 :

| Effort sélectionné dans Claude Code | Effort effectif dans GLM-5.2 |
| --- | --- |
| `low`, `medium`, `high` (défaut) | `high` |
| `xhigh`, `max`, `ultracode` | `max` |

Pour les tâches de code, l'usage de l'effort `max` est recommandé pour un raisonnement plus profond et des performances plus stables sur les tâches complexes.

**FAQ.** Pour vérifier quel modèle est utilisé : ouvrir un nouveau terminal, lancer `claude`, puis entrer `/status`. La doc mentionne aussi un Vision Search Reader MCP (Vision MCP Server) référencé dans la documentation de Z.ai.

## Pourquoi ça compte

C'est la preuve concrète que le harnais (Claude Code) est découplé du modèle : un modèle chinois open-weight 20× moins cher s'y branche en quelques réglages. La portabilité du modèle devient une réalité opérationnelle, pas une promesse.
