# Runbook

## Deploy
1. Copy `.env.example` to `.env` and set a strong local password.
2. Run `docker compose config --quiet`.
3. Run `docker compose up -d --build`.
4. Confirm `docker compose ps` shows DB and API healthy.
5. Verify `http://localhost:8000/health` and `/ready`.

## Investigate
1. Capture `docker compose ps` and logs before changes.
2. Check `/health` (process) and `/ready` (database dependency).
3. Inspect `docker compose logs --tail 100 api` and `docker compose logs --tail 100 db`.
4. Verify `.env` password consistency and DB health; change one thing at a time.
5. Re-check readiness and record actual output.

## Stop
`docker compose down` preserves DB volume. `docker compose down -v` deletes demo data too.
