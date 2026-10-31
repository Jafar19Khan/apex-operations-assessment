# Apex Operations API

Small Flask API backed by PostgreSQL. The project is set up to run locally with Docker Compose and to run linting, tests and an image build through Jenkins.

## What is included

- Flask API with `/health`, `/ready`, `/items` and `/metrics` endpoints
- PostgreSQL database with a named volume
- Docker image that runs the API as a non-root user
- Compose health checks for the database and API
- Jenkins pipeline for linting, tests and image build
- Versioned image deployment and rollback instructions in `docs/rollback.md`

This is a local assessment project. It does not include a cloud deployment or a running Prometheus server.

## Run it locally

Requirements: Git, PowerShell and Docker Desktop running Linux containers.

```powershell
Copy-Item .env.example .env
notepad .env
docker compose config --quiet
docker compose up -d --build
docker compose ps
```

Set `POSTGRES_PASSWORD` in `.env` to a strong password made of letters, numbers, and hyphens. Keeping it to those characters avoids URL-encoding issues in the local `DATABASE_URL`. Do not commit `.env`.

Wait until the API and database report healthy, then check the endpoints:

```powershell
Invoke-RestMethod http://localhost:8000/health
Invoke-RestMethod http://localhost:8000/ready
Invoke-RestMethod http://localhost:8000/items
```

Create a sample item:

```powershell
$body = @{ name = 'Assessment demo item' } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://localhost:8000/items -ContentType 'application/json' -Body $body
Invoke-RestMethod http://localhost:8000/items
```

Metrics are available at `http://localhost:8000/metrics`. This endpoint exposes Prometheus-format data; the repository includes example scrape and alert-rule files, but no Prometheus server or alert receiver is started by Compose.

## Run checks

The CI Dockerfile installs the project requirements, runs Ruff and executes the regular test suite:

```powershell
docker build -f Dockerfile.ci -t apex-operations-ci:local .
```

The normal suite excludes one deliberately failing test used for the CI failure-gate demonstration. To run that test separately, the command is expected to return a failure:

```powershell
docker run --rm -v "${PWD}:/workspace" -w /workspace python:3.12-slim sh -c "pip install -r requirements.txt && python -m pytest -q -m intentional_failure"
```

Do not treat the expected failure as a defect in the normal test run.

## Jenkins

Start the optional Jenkins service:

```powershell
docker compose --profile ci up -d --build jenkins
docker compose --profile ci exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Open `http://localhost:8081`, complete the initial setup, then create a Pipeline job using **Pipeline script from SCM**. Select Git, enter this repository URL, set the branch to `*/main`, and use `Jenkinsfile` as the script path.

The Jenkins container mounts the host Docker socket so it can build images. Access to that socket is effectively privileged. Keep this Jenkins instance local and do not expose it to an untrusted network.

## Release and rollback

Use the versioned image commands in `docs/rollback.md`. Keep the previous known-good image tag available locally. After deploying or rolling back, check both `/health` and `/ready`.

## Stop the services

```powershell
docker compose --profile ci down
```

The database volume is retained. To remove the local database data as well:

```powershell
docker compose --profile ci down -v
```

## Notes

- PostgreSQL is not published on a host port; the API reaches it over the Compose network.
- The API is published on `127.0.0.1:8000`.
- `/health` checks that the API process responds. `/ready` also checks the database.
- The API writes logs to standard output/error so they can be read with `docker compose logs`.
- Complete `AI_DISCLOSURE.md` honestly to reflect the assistance used and the work you personally reviewed and ran.
