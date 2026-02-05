# T11PRH96

My portfolio - FastAPI backend + React frontend application with Docker support.

## Project Structure

```
t11prh96/
├── backend/               # FastAPI backend
│   ├── main.py           # Main application
│   ├── pyproject.toml    # Backend dependencies
│   ├── Dockerfile        # Production Docker image
│   └── Dockerfile.dev    # Development Docker image
├── frontend/             # React frontend (à configurer)
├── pyproject.toml        # Workspace root configuration
├── uv.lock              # Dependency lock file
├── docker-compose.yml    # Production compose
└── docker-compose.dev.yml # Development compose
```

## Prerequisites

- [uv](https://docs.astral.sh/uv/) - Python package manager
- Docker & Docker Compose
- Node.js 20+ (pour le frontend)

## Local Development (sans Docker)

### Backend

```bash
# Installer uv si nécessaire
curl -LsSf https://astral.sh/uv/install.sh | sh

# Ajouter uv au PATH (ou redémarrer le terminal)
export PATH="$HOME/.local/bin:$PATH"

# Synchroniser les dépendances
uv sync

# Lancer le backend en mode dev (avec hot-reload)
uv run fastapi dev backend/main.py

# Ou en mode production
uv run fastapi run backend/main.py
```

Le backend sera accessible sur http://localhost:8000

- API: http://localhost:8000
- Documentation interactive: http://localhost:8000/docs
- Health check: http://localhost:8000/health

## Docker Development

### Backend seulement

```bash
# Build et lancer avec docker-compose (dev)
docker compose -f docker-compose.dev.yml up backend

# Ou manuellement
docker build -f backend/Dockerfile.dev -t t11prh96-backend:dev .
docker run -p 8000:8000 -v $(pwd)/backend:/app/backend t11prh96-backend:dev
```

### Backend + Frontend

```bash
# Lancer tous les services en dev
docker compose -f docker-compose.dev.yml --profile frontend up

# Ou en production
docker compose up
```

## Docker Production

```bash
# Build production image
docker build -f backend/Dockerfile -t t11prh96-backend:latest .

# Run production container
docker run -p 8000:8000 t11prh96-backend:latest

# Ou avec docker-compose
docker compose up -d
```

## Commandes utiles

```bash
# Ajouter une dépendance au backend
uv add --package backend nouvelle-package

# Mettre à jour les dépendances
uv sync

# Voir les dépendances installées
uv pip list

# Lancer les tests (à configurer)
uv run pytest

# Voir les logs Docker
docker compose logs -f backend
```

## Configuration

### Variables d'environnement

Créez un fichier `.env` à la racine du projet:

```env
# Backend
ENV=development
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
REDIS_URL=redis://localhost:6379

# Frontend
VITE_API_URL=http://localhost:8000
```

## API Endpoints

- `GET /` - Message de bienvenue
- `GET /health` - Health check

Documentation complète: http://localhost:8000/docs
