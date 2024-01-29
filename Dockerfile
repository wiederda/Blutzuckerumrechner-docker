# Verwende das offizielle Python-Image als Basis
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Python-Skriptdateien in das Arbeitsverzeichnis
COPY app.py .
COPY templates templates

RUN chmod -R 777 /app

# Installiere die erforderlichen Python-Pakete
RUN pip install Flask gunicorn

# Öffne den Port 5000
EXPOSE 80

# Starte den Gunicorn-Webserver beim Containerstart
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
