# Utilisez l'image Python 3.11 officielle
FROM python:3.11

# Créez et définissez un répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de dépendances (comme requirements.txt) dans le conteneur
COPY requirement.txt .

# Installez les dépendances
RUN pip install --no-cache-dir -r requirement.txt

# Copiez le reste du code source de l'application dans le conteneur
COPY . .

# Exécutez FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]