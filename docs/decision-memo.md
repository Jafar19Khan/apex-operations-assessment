# Decision memo

Use Flask, PostgreSQL, Docker Compose and Jenkins for a reproducible local delivery path. Compose starts the API and persistent database; Jenkins runs lint, tests and image build. The API provides process health, DB readiness and Prometheus-format metrics. No cloud deployment is included because the assessment requests local reproducibility and prohibits paid resources. Prometheus server/alerts, image scanning and an executed rollback remain validation steps rather than claimed outcomes.
