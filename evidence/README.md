# Apex Operations DevOps Assessment — Evidence Pack

The following screenshots document the local Jenkins CI pipeline, Docker deployment, API verification, rollback and failure-gate demonstration.

| File | Evidence |
|---|---|
| 01-jenkins-build-success-console.png | Jenkins successful build console |
| 02-jenkins-pipeline-stages.png | Jenkins pipeline stages |
| 03-jenkins-job-overview.png | Jenkins job and build history |
| 04-deployed-image-tag.png | Versioned Docker image deployed |
| 05-compose-services-healthy.png | API and database health status |
| 06-api-health-endpoint.png | GET /health response |
| 07-api-readiness-endpoint.png | GET /ready response |
| 08-prometheus-metrics-endpoint.png | API Prometheus-format metrics |
| 09-rollback-to-previous-image.png | Previous image rollback |
| 10-restore-version-5-and-compose-health.png | Version 5 restored and services checked |
| 11-intentional-test-failure.png | Deliberately failing pytest demonstration |
| 12-jenkins-failure-gate-blocks-build.png | Jenkins blocks the image build after test failure |
| 13-jenkins-final-job-status-build-11.png | Jenkins final job status |
| 14-normal-test-execution.png | Normal test suite: 8 passed, 1 deselected |
| 15-jenkins-build-11-console-success.png | Jenkins Build #11 successful console output |

## Evidence limitations

- The failure-gate demonstration is intentionally expected to fail.
- The normal test suite excludes the intentional-failure test.
- The supplied metrics screenshot proves that the API exposes metrics; it does not prove that a Prometheus server is running.
- Prometheus scrape and alert rule files are configuration proposals, not evidence of active alert delivery.
- Screenshots should be interpreted together with the source, runbook and CI configuration.
