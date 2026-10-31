# Apex Operations Architecture

```mermaid
flowchart TD
    A[Developer] --> B[GitHub Repository]
    B --> C[Jenkins CI Pipeline]
    C --> D[Ruff Lint]
    D --> E[Pytest Automated Tests]
    E --> F{Tests Passed?}
    F -->|No| G[Pipeline Failed - Stop Release]
    F -->|Yes| H[Build Versioned Docker Image]
    H --> I[Docker Compose Deployment]
    I --> J[Flask API]
    J --> K[PostgreSQL Database]
    J --> L[/health]
    J --> M[/ready]
    J --> N[/metrics]
    N --> O[Prometheus Scraping Proposal]
    O --> P[Alert Rules Proposal]
    I --> Q[Persistent Database Volume]
    H --> R[Previous Image Version]
    R --> S[Rollback]
