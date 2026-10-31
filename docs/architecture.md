# Architecture

Local user -> Flask API (`127.0.0.1:8000`) -> PostgreSQL 16 on a private Compose network. PostgreSQL data persists in a named volume. The API exposes `/health`, database-aware `/ready`, and Prometheus-format `/metrics`. Jenkins is an optional local CI service: checkout -> Ruff -> pytest -> Docker image build.

A Prometheus server, scrape configuration and alert receiver are not included. Jenkins mounts the local Docker socket to build images; this is privileged and suitable only for an isolated local assessment machine. No cloud deployment or paid resource is required.
