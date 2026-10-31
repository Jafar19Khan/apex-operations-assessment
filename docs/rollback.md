# Versioned release and rollback

Build a versioned image and deploy it using the release override:

```powershell
docker build -t apex-operations-api:v1 .
$env:API_IMAGE = 'apex-operations-api:v1'
docker compose -f docker-compose.yml -f compose.release.yml up -d --no-build
Invoke-RestMethod http://localhost:8000/ready
```

For the next release, build and deploy `apex-operations-api:v2` in the same way. Keep the previous tag locally. To roll back, point `API_IMAGE` to the previous known-good tag and redeploy:

```powershell
$env:API_IMAGE = 'apex-operations-api:v1'
docker compose -f docker-compose.yml -f compose.release.yml up -d --no-build
Invoke-RestMethod http://localhost:8000/health
Invoke-RestMethod http://localhost:8000/ready
```

Record the actual image IDs and command output. A rollback is not claimed as demonstrated until these steps have been executed successfully.
