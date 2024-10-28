# Ayomi NPI test technique

## Projet FastAPI et React avec Docker

### Auteur : Blaise Antonio IRADUKUNDA

Ce projet combine un backend en FastAPI et un frontend en React, tous deux conteneurisés avec Docker.

## Prérequis

Avant de lancer l'application, assurez-vous que :
- Docker est installé sur votre machine.
- L'extension Docker Compose est également installée.

## Lancer l'application

Pour démarrer l'application, suivez ces étapes :

1. **Vérification des ports** : Assurez-vous qu'aucun autre processus n'utilise les ports `8000` (backend) et `3000` (frontend).

2. **Démarrage avec Docker Compose** :
   ```bash
   docker compose up -d --build
   ```
    Cette commande construit les images Docker et démarre les conteneurs.
- Construit les conteneurs pour le frontend et le backend.
- Démarre l'application en arrière-plan.

## Accès aux services

- **Backend (FastAPI)** : accessible via [http://localhost:8000](http://localhost:8000)
- **Frontend (React)** : accessible via [http://localhost:3000](http://localhost:3000)

### Documentation des Routes

La documentation interactive des routes de l'API backend est disponible à l'adresse suivante :

- [http://localhost:8000/docs](http://localhost:8000/docs)

