# GIC Bénie

Site public de GIC Bénie, école maternelle et primaire en Côte d'Ivoire.

> Projet en cours : phase 0 (fondations).

## Pile technique

- Python 3.12+, Django 6.1
- uv (dépendances et environnement)
- SQLite (développement)
- pytest et Ruff

## Installer le projet

Prérequis : [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/<CyrilleAD>/gic-benie.git
cd gic-benie
uv sync
cp .env.example .env    # puis générer une clé (voir .env.example)
uv run python manage.py migrate
```

## Lancer en local

```bash
uv run python manage.py runserver
```

Puis ouvrir http://127.0.0.1:8000.

## Vérifier

```bash
uv run pytest
uv run ruff check .
```
