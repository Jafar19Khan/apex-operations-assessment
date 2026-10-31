# Apex Operations API — Junior DevOps Assessment

A minimal Flask API with PostgreSQL, Docker Compose, Jenkins CI, automated checks, health/readiness endpoints and Prometheus-format metrics.

## Requirements
Windows PowerShell, Git and Docker Desktop using Linux containers. No AWS account or paid cloud service is required for this local assessment.

## Start locally
```powershell
Copy-Item .env.example .env
notepad .env
# Replace the placeholder with a strong local-only password; never commit .env.
docker compose config --quiet
docker compose up -d --build
docker compose ps
```
Wait for DB and API to become healthy.

## Verify live API
```powershell
Invoke-RestMethod http://localhost:8000/health
Invoke-RestMethod http://localhost:8000/ready
Invoke-RestMethod http://localhost:8000/items
$body = @{ name = 'Assessment demo item' } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://localhost:8000/items -ContentType 'application/json' -Body $body
Invoke-RestMethod http://localhost:8000/items
```
Metrics: `http://localhost:8000/metrics`.

## Local checks
```powershell
docker run --rm -v "${PWD}:/workspace" -w /workspace python:3.12-slim sh -c "pip install -r requirements.txt && ruff check app tests && python -m pytest -q"
```
The default test suite excludes a separately marked intentional-failure test. Demonstrate the negative test gate with this expected-to-fail command:
```powershell
docker run --rm -v "${PWD}:/workspace" -w /workspace python:3.12-slim sh -c "pip install -r requirements.txt && python -m pytest -q -m intentional_failure"
```

## Jenkins CI
Push this repository to GitHub first. Start Jenkins:
```powershell
docker compose --profile ci up -d --build jenkins
docker compose --profile ci exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```
Open `http://localhost:8081`, complete setup and install suggested plugins (Pipeline and Git). Create **New Item → Pipeline**. Select **Pipeline script from SCM**, Git, your repository URL, branch `*/main`, script path `Jenkinsfile`; save and Build Now. Pipeline runs checkout, Ruff, pytest and Docker image build. Jenkins uses the local Docker socket; this is privileged and for isolated local assessment use only.

## Rollback and operations
Follow `docs/rollback.md` for the exact PowerShell commands to build versioned image tags, deploy a release and roll back to the previous tag. Verify `/health` and `/ready`; do not claim rollback until actually demonstrated and evidenced.

## Stop
```powershell
docker compose down
# To also delete persisted demo DB data:
docker compose down -v
docker compose --profile ci down
```

## Architecture and limitations
PowerShell/browser -> API on loopback port 8000 -> PostgreSQL on private Compose network with named volume. GitHub source -> Jenkins -> Ruff/pytest -> Docker build. `/metrics` is Prometheus exposition format; no Prometheus server, scrape configuration or alert receiver is included. The API logs to container stdout/stderr. This is a local assessment demo, not a production customer-data service. Complete `AI_DISCLOSURE.md` accurately and save only real execution evidence under `evidence/`.
