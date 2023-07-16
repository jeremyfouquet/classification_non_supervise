# Classification non supervisé avec K-means de compétences en informatique

## Version

1.0.0

## Description

Ce proggramme utilise une classification non supervisé avec K-means sur un corpus de compétences issus de 30 métiers du secteur de l'informatique afin de tenter de prédire un groupe de métiers correspondant pour une nouvelle liste de compétences.

## Auteur

Jeremy Fouquet

## Exigences

- Avoir Python3 sur la machine
- Pour installer Python3 suivre les instructions du site officiel https://www.python.org/
- Version Python utilisé 3.8.2

## Utilisation

Executer le programme
```
$ make run
```

Desinstaller l'environnement virtuel et le cache
```
$ make clean
```

## Structure
    .
    ├── main.py : Point d'entrée et code source du programme
    ├── Makefile : Directives d'automatisation d'installation des dépendances, d'execution du programme et de désinstallation
    ├── Makefile : contient les directives d'automatisation de tests, de nettoyage, d'installation de dépendances et de lancement du
    ├── requirements.txt : Contient les dépendances et version nécessaires à installé dans l'environnement virtuel
    └── README.md : Documentation technique
