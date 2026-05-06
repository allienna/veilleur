---
title: "AI didn't delete your database, you did"
date: 2026-05-06
url: https://idiallo.com/blog/ai-didnt-delete-your-database-you-did
authors: [Ibrahim Diallo]
keywords: [accountability, IA, garde-fous, automatisation, CI/CD]
theme: IA
tone: opinion
used_in: ["2026-05-06"]
---

## Résumé

Suite au thread viral d'un développeur dont l'agent Cursor/Claude a supprimé la base de production, Ibrahim Diallo répond sèchement : ce n'est pas l'IA qui a effacé ta base, c'est toi qui as un endpoint capable de le faire. La leçon est ancienne : en 2010, Diallo lui-même a effacé un repo SVN par erreur — la réponse de son lead n'a pas été de blâmer l'humain, mais de mettre en place un script qui rendait l'erreur impossible. L'automatisation et les garde-fous éliminent les erreurs bêtes. L'IA n'est pas magique : elle exécute ce qu'on lui permet d'exécuter.

## Points clés

- L'IA n'a pas supprimé ta base — toi (ou ton organisation) lui as donné le pouvoir de le faire
- Pourquoi un agent a-t-il une permission de drop production ? La vraie question
- Diallo (2010) : a effacé `trunk` en SVN — la solution n'a pas été le blâme, mais un CI/CD
- L'automatisation élimine les erreurs bêtes ; l'IA les amplifie sans garde-fous
- Le pattern de réaction "blâme l'outil" empêche la mise en place des bonnes barrières
- Penser en termes de blast radius : qu'est-ce que cette action peut casser au pire ?

## Analyse approfondie

La semaine dernière, un tweet est devenu viral. Un type montrait qu'un agent Cursor/Claude avait supprimé la base de production de son entreprise. On l'a regardé essayer d'arracher une confession à l'agent : "Pourquoi as-tu supprimé alors qu'on t'avait dit de ne jamais faire ça ?" Puis il a essayé de parser la réponse pour soit en tirer une leçon, soit nous avertir des dangers des agents IA.

Diallo a aussi une question : pourquoi as-tu un endpoint d'API qui supprime ta base de production entière ? Le post du gars rumine sur le marketing trompeur de l'IA, le mauvais support client, etc. Ce qui manque, c'est l'accountability.

Diallo n'est pas du genre à défendre l'IA aveuglément ; il penche toujours du côté de la prudence. Mais on ne peut pas blâmer un outil pour ses propres erreurs.

### 2010 : SVN et le double `trunk`

En 2010, Diallo travaillait pour une boîte avec un processus de déploiement très manuel. Ils utilisaient SVN. Pour déployer, il fallait copier `trunk` (l'équivalent de la branche master) dans un dossier release labellisé avec la date. Puis on faisait une seconde copie de cette release, qu'on appelait "current". De cette façon, tirer le dossier `current` donnait toujours la dernière release.

Un jour, en déployant, Diallo a accidentellement copié `trunk` deux fois. Pour réparer via la CLI, il a édité sa commande précédente pour supprimer le doublon. Puis il a continué le déploiement sans incident... du moins le pensait-il. En fait, il n'avait pas supprimé le double : il avait édité la mauvaise commande et supprimé `trunk` à la place. Plus tard ce jour-là, un autre développeur a été surpris de ne pas le retrouver.

L'enfer s'est déchaîné. Les managers ont couru, des réunions ont été déclenchées. Le temps que la nouvelle remonte à son équipe, le lead developer avait déjà lancé une commande pour annuler la suppression. Il a vérifié les logs, vu que Diallo était responsable, et la tâche suivante de Diallo a été d'**écrire un script pour automatiser le processus de déploiement**, pour que ce genre d'erreur ne puisse plus se produire. Avant la fin de la journée, ils avaient un système plus robuste en place. Un système qui s'est ensuite étendu en pipeline CI/CD complet.

> *L'automatisation aide à éliminer les erreurs bêtes.*

### Le parallèle avec l'IA

Quand un agent IA supprime une prod, la réaction réflexe est de blâmer l'agent. Mais cette réaction est exactement la même que celle qui aurait blâmé Diallo en 2010. Et elle est aussi peu utile.

Les bonnes questions sont :
- **Pourquoi cette permission existait-elle ?** Pourquoi un endpoint capable de drop production était accessible depuis le périmètre de l'agent ?
- **Pourquoi pas de confirmation à deux facteurs ?** Pourquoi pas de dry-run obligatoire ? Pourquoi pas de fenêtre de blast radius ?
- **Pourquoi pas de backup à T-5min ?** Quel processus de restore avait-on ?
- **Pourquoi cet agent avait-il les credentials de prod ?** Qui les lui a donnés et pourquoi ?

Ces questions ne pointent pas vers l'IA. Elles pointent vers une organisation qui n'a pas mis en place les garde-fous appropriés. L'IA agit selon ce qu'on lui permet — exactement comme un humain.

### L'IA amplifie ce qui était déjà cassé

Le piège de l'IA, c'est qu'elle agit vite. Là où un humain aurait pu hésiter, demander confirmation, faire une pause, l'agent exécute. Si tes garde-fous reposaient sur l'hésitation humaine — sur le fait que personne ne pousserait sur "Yes, drop production" sans relire trois fois — alors l'IA va casser ton système, parce qu'elle ne hésite pas.

Mais ce n'est pas une critique de l'IA. C'est un signal que tes garde-fous étaient en réalité absents : ils étaient juste invisibles tant que les humains compensaient. L'IA rend visible cette absence.

### Les garde-fous qui marchent

Diallo ne donne pas une liste exhaustive, mais le pattern est clair :
- **Capability-based permissions** : un agent ne devrait avoir que les permissions strictement nécessaires à sa tâche, pas plus
- **Confirmation explicite pour les actions destructrices** : un dry-run, ou une approbation humaine, pour tout ce qui est irréversible
- **Blast radius limité** : une action ne peut affecter qu'un sous-périmètre clairement délimité
- **Logs immuables et alertes** : pour détecter une erreur en cours et la rattraper avant qu'elle ne se propage
- **Restore testé** : le backup ne sert à rien s'il n'a jamais été restauré pour de vrai

Aucune de ces pratiques n'est nouvelle. Elles existent en sécurité depuis 30 ans. Ce qui est nouveau, c'est qu'on doit les appliquer à des entités qui ne sont ni humaines, ni des scripts à comportement déterministe : des agents probabilistes.

## Pourquoi ça compte

Cet article remet l'accountability au centre du débat sur les incidents IA. À chaque fois qu'un agent "cause" un dommage, la première question doit être : qui a configuré le système qui a permis ce dommage ? Lecture salutaire pour toute équipe qui déploie des agents en production sans avoir d'abord audité son périmètre de permissions.
