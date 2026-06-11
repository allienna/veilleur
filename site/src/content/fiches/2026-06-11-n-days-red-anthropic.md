---
title: "N-days \\ red.anthropic.com"
date: 2026-06-11
url: https://red.anthropic.com/2026/n-days/?utm_source=tldrai
authors: [red.anthropic.com, Winnie Xiao, Tim Abbott, Nicholas Carlini, Newton Cheng, David Forsythe, Keane Lucas, Milad Nasr, Shikhar Sakhuja]
keywords: [cybersécurité, N-days, exploits, LLM, patch gap, red team]
theme: IA
tone: research
used_in: ["2026-06-11"]
---

## Résumé

L'équipe red team d'Anthropic publie une étude sur la capacité des LLMs à développer des exploits pour des N-days — des vulnérabilités déjà divulguées publiquement mais pas encore patchées sur tous les systèmes. Résultat : Claude Mythos Preview a construit de manière autonome 8 exploits fonctionnels sur 18 patches Firefox récents, et 8 chaînes d'exploitation complètes sur 21 patches Windows kernel. Cette accélération menace de compresser drastiquement le "patch gap" — la fenêtre historique de plusieurs semaines dont disposaient les défenseurs pour déployer leurs mises à jour.

## Points clés

- Les N-days (vulnérabilités divulguées mais non patchées partout) causent une grande partie des dommages réels en cybersécurité
- Historiquement, le "patch gap" durait plusieurs semaines (WannaCry : 59 jours après MS17-010, Citrix Bleed : ~2 semaines)
- Claude Mythos Preview : 8/18 exploits Firefox, 8/21 chaînes complètes Windows kernel, en autonomie
- Les modèles publics — avec les safeguards désactivés — peuvent aussi construire des exploits, même si moins nombreux
- La "patch diffing" (comparaison avant/après patch pour localiser la vulnérabilité) est maintenant automatisable par LLM

## Analyse approfondie

### Les N-days : le danger méconnu

Pour la plupart des gens, les zero-days (vulnérabilités inconnues des mainteneurs) semblent être la menace la plus critique. Mais une grande partie des dommages réels en cybersécurité provient des N-days : des vulnérabilités qui ont déjà été divulguées publiquement, mais qui n'ont été patchées que sur une partie des systèmes. Les attaquants exploitent les nombreux systèmes qui n'ont pas encore appliqué le patch, pendant ce qu'on appelle le "patch gap".

D'une certaine façon, les N-days sont les plus dangereuses des deux, car le patch lui-même fournit une feuille de route vers le bug. Une fois que les éditeurs publient leurs mises à jour de sécurité, les attaquants peuvent faire du "patch diffing" : comparer le code source ou le binaire avant et après le patch pour localiser exactement ce qui a changé, puis retrouver par ingénierie inverse la vulnérabilité que le patch était censé corriger.

### Le contexte historique

Historiquement, le patch diffing était un travail lent et spécialisé, ce qui donnait aux défenseurs le temps de déployer largement leurs mises à jour. Les incidents dont la plupart des défenseurs se souviennent prenaient plusieurs semaines :

- WannaCry a frappé 59 jours après MS17-010 en 2017
- L'exploit public pour Citrix Bleed en 2023 a pris environ deux semaines
- Dans l'analyse Mandiant de 2020 sur les N-days, 16 des 25 vulnérabilités ont pris un mois ou plus à exploiter

### Les résultats de l'étude

L'équipe a évalué dans quelle mesure les LLMs peuvent accélérer et automatiser le processus de développement d'exploits N-day. Le développement d'exploits n'est pas la seule étape d'une vraie campagne N-day (la découverte de cibles, la livraison de l'exploit à la cible, et l'évasion de détection prennent aussi du temps et des ressources), mais c'est historiquement l'étape la plus contrainte par la rareté des experts en reverse engineering.

Avec les modèles frontier, ce goulot d'étranglement a largement disparu :

**Firefox (code source disponible) :**
- Claude Mythos Preview : 8 exploits fonctionnels sur 18 patches récents
- Les exploits incluent des vulnérabilités d'exécution de code arbitraire

**Windows kernel (sans accès au code source) :**
- Claude Mythos Preview : 8 chaînes d'exploitation complètes sur 21 patches
- Ces chaînes escaladaient un utilisateur à faibles privilèges jusqu'au contrôle SYSTEM complet

L'étude montre également que les modèles publics — avec les safeguards désactivés — peuvent aussi construire des exploits, même si en moins grand nombre que Mythos Preview. Cela suggère que n'importe qui disposant d'un accès aux modèles publics et désireux de désactiver les protections peut accéder à des capacités d'exploitation significatives.

### Les implications pour le patch gap

La conséquence directe : le patch gap — cette fenêtre de temps précieuse dont les équipes de sécurité disposaient pour déployer leurs correctifs avant que les attaquants ne construisent des exploits — est en train d'être compressée de semaines à potentiellement quelques heures.

Pour les équipes de sécurité, cela signifie que les workflows de patching qui "fonctionnaient" dans un monde pré-LLM ne sont plus suffisamment rapides. La priorité aux patches critiques doit être revue à la lumière de cette accélération.

### La transparence d'Anthropic

Ce qui est notable dans cette publication : c'est Anthropic eux-mêmes qui publient ces résultats, sachant très bien qu'ils documentent les capacités offensives de leurs propres modèles. Cette transparence est cohérente avec leur approche de "responsible scaling policy" et leur travail de red team, mais elle illustre aussi la tension fondamentale de leur position.

## Pourquoi ça compte

Cette étude redéfinit l'urgence de la posture défensive en cybersécurité. Le "patch gap" était le pilier implicite sur lequel reposait toute la stratégie de patching. Si les LLMs le compriment à quelques heures, les organisations qui n'ont pas de capacité de déploiement quasi-immédiat des patches critiques sont significativement plus exposées qu'elles ne le réalisent.
