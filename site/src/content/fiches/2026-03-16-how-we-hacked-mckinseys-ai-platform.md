---
title: "How We Hacked McKinsey's AI Platform"
date: 2026-03-16
url: https://leadershipintech.com/links/21763/3d78f33c-7ca0-4e03-9c70-68e56918a4cd/email
authors: [Leadership in Tech]
keywords: [McKinsey, Lilli, AI security, penetration testing, autonomous agent]
theme: IA
tone: opinion
used_in: ["2026-03-16"]
---

## Résumé

McKinsey a construit Lilli, une plateforme IA interne pour ses 43 000+ employés : chat, analyse de documents, RAG sur des décennies de recherche propriétaire, recherche IA sur 100 000+ documents internes. Une équipe de sécurité offensive a pointé un agent autonome dessus — sans credentials, sans connaissance interne, sans intervention humaine — juste un nom de domaine.

## Points clés

- Lilli est une plateforme IA interne de McKinsey utilisée par 70 % des employés, traitant 500 000+ prompts/mois
- L'attaque a été menée par un agent autonome sans credentials ni connaissance préalable
- La plateforme a accès à 100 000+ documents internes et des décennies de recherche propriétaire
- Cela illustre que la sophistication du modèle IA ne compense pas les failles d'infrastructure
- La surface d'attaque augmente avec chaque document indexé dans le système RAG

## Analyse approfondie

McKinsey & Company — le cabinet de conseil le plus prestigieux au monde — a construit une plateforme IA interne appelée **Lilli** pour ses 43 000+ employés. Lilli est un système conçu spécifiquement : chat, analyse de documents, RAG sur des décennies de recherche propriétaire, recherche alimentée par l'IA sur plus de 100 000 documents internes. Lancée en 2023, nommée d'après la première femme professionnelle embauchée par le cabinet en 1945, adoptée par plus de 70 % de McKinsey, traitant plus de 500 000 prompts par mois.

Une équipe de sécurité offensive a donc décidé de pointer leur agent offensif autonome dessus. Sans credentials. Sans connaissance interne. Et sans intervention humaine. Juste un nom de domaine et un objectif.

Le résultat est un rappel brutal que les fondations de sécurité comptent autant pour les plateformes IA que pour n'importe quel autre système. Peu importe la sophistication de votre modèle, peu importe la qualité de votre RAG, si l'infrastructure qui porte le tout est vulnérable, l'ensemble est vulnérable.

Ce qui rend ce cas particulièrement préoccupant, c'est l'ampleur de la surface d'attaque. Quand une plateforme IA a accès à 100 000 documents internes couvrant des décennies de conseil stratégique pour les plus grandes entreprises du monde, une compromission n'est pas juste un incident technique — c'est une fuite potentielle de propriété intellectuelle d'une valeur incalculable.

La dette de sécurité dans les systèmes IA est particulièrement insidieuse : elle s'accumule silencieusement à chaque nouveau document indexé, à chaque nouvelle intégration ajoutée, à chaque nouveau cas d'usage activé. Et contrairement à la dette technique classique, elle ne se manifeste pas par de la friction quotidienne — elle se révèle d'un coup, quand quelqu'un exploite la faille.

## Pourquoi ça compte

Ce cas illustre que la sécurité des plateformes IA d'entreprise est un angle mort majeur. Alors que les organisations se précipitent pour déployer des systèmes RAG sur leurs données les plus sensibles, les audits de sécurité spécifiques à l'IA restent rares.
