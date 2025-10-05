# Expenza Backend API

API REST Django pour l'application de gestion de transactions Expenza.

## 🚀 Démarrage Rapide

### Prérequis

- Python 3.10 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation

1. **Cloner le projet**
```bash
git clone <url-du-repo>
cd backend
```

2. **Créer un environnement virtuel**
```bash
python -m venv env
```

3. **Activer l'environnement virtuel**

**Linux/Mac :**
```bash
source env/bin/activate
```

**Windows :**
```bash
env\Scripts\activate
```

4. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

5. **Créer le fichier .env**
```bash
touch .env
```

Ajouter dans `.env` :
```env
SECRET_KEY=votre-cle-secrete-django-ici
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

6. **Appliquer les migrations**
```bash
python manage.py migrate
```

7. **Créer un superutilisateur (optionnel)**
```bash
python manage.py createsuperuser
```

8. **Démarrer le serveur**
```bash
python manage.py runserver
```

Le serveur démarre sur **http://localhost:8000**

## 📚 Documentation API

Une fois le serveur démarré, accédez à :

- **Swagger UI** : http://localhost:8000/swagger/
- **ReDoc** : http://localhost:8000/redoc/
- **Admin Django** : http://localhost:8000/admin/

## 🔑 Endpoints Principaux

### Authentification

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/auth/register/` | Inscription d'un nouvel utilisateur |
| POST | `/api/auth/login/` | Connexion |
| POST | `/api/auth/logout/` | Déconnexion |
| GET | `/api/auth/user/` | Récupérer le profil utilisateur |
| POST | `/api/auth/token/refresh/` | Rafraîchir le token JWT |
| POST | `/api/auth/change-password/` | Changer le mot de passe |

### Transactions

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/transactions/` | Liste des transactions |
| POST | `/api/transactions/` | Créer une transaction |
| GET | `/api/transactions/{id}/` | Détails d'une transaction |
| PUT/PATCH | `/api/transactions/{id}/` | Modifier une transaction |
| DELETE | `/api/transactions/{id}/` | Supprimer une transaction |

## 📦 Structure du Projet

```
backend/
├── api/
│   ├── models/          # Modèles de données (User, Transaction)
│   ├── serializers/     # Serializers DRF
│   ├── views/           # Vues API
│   └── urls.py          # Routes API
├── core/
│   ├── settings.py      # Configuration Django
│   └── urls.py          # Routes principales
├── manage.py
└── requirements.txt
```

## 🔧 Configuration

### Base de données

Par défaut, le projet utilise **SQLite** en développement.

Pour utiliser **PostgreSQL** en production, configurez la variable d'environnement :
```env
DATABASE_URL=postgresql://user:password@localhost:5432/expenza
```

### CORS

Les origines autorisées sont configurées dans `core/settings.py` :
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3000",
]
```

### JWT Tokens

- **Access Token** : expire après 1 heure
- **Refresh Token** : expire après 7 jours

## 🧪 Tests

Pour exécuter les tests :
```bash
python manage.py test
```

## 📝 Modèles de Données

### User
- `email` - Email unique (utilisé pour la connexion)
- `first_name` - Prénom
- `last_name` - Nom
- `phone` - Téléphone (optionnel)
- `password` - Mot de passe hashé

### Transaction
- `id` - UUID
- `user` - Relation vers User
- `text` - Description de la transaction
- `amount` - Montant (positif = revenu, négatif = dépense)
- `created_at` - Date de création
- `updated_at` - Date de modification

## 🛠️ Commandes Utiles

```bash
# Créer des migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Collecter les fichiers statiques
python manage.py collectstatic

# Lancer le shell Django
python manage.py shell
```

## 🚀 Déploiement

Pour déployer en production :

1. Désactiver le mode DEBUG
```env
DEBUG=False
```

2. Configurer ALLOWED_HOSTS
```env
ALLOWED_HOSTS=votre-domaine.com,www.votre-domaine.com
```

3. Utiliser Gunicorn
```bash
gunicorn core.wsgi:application --bind 0.0.0.0:8000
```

## 📄 Technologies

- Django 5.2.6
- Django REST Framework 3.16.1
- djangorestframework-simplejwt 5.3.1
- django-cors-headers 4.9.0
- drf-yasg 1.21.7
- PostgreSQL / SQLite
- Argon2 (hashage des mots de passe)

## 📞 Support

Pour toute question ou problème, consultez la documentation Swagger ou contactez l'équipe de développement.
