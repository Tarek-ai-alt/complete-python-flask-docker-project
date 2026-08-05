# Complete Python Flask Docker Project

## Project requirements

Install:

- Docker Desktop
- Visual Studio Code

## Open in Visual Studio Code

1. Extract the ZIP file.
2. Open Visual Studio Code.
3. Select **File > Open Folder**.
4. Open the extracted project folder.
5. Open **Terminal > New Terminal**.

## Start with Docker Compose

```bash
docker compose up --build -d
```

Open:

```text
http://localhost:5000
```

Health endpoint:

```text
http://localhost:5000/health
```

## View logs

```bash
docker compose logs -f
```

## Stop the application

```bash
docker compose down
```

## Run using Docker commands

Build:

```bash
docker build -t flask-app .
```

Run:

```bash
docker run -d --name flask-app -p 5000:5000 flask-app
```

View logs:

```bash
docker logs -f flask-app
```

Stop and remove:

```bash
docker stop flask-app
docker rm flask-app
```

## Run locally without Docker

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Start the application:

```powershell
python run.py
```

## Run tests

```powershell
pytest
```
# complete-python-flask-docker-project
