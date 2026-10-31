# Apex Operations DevOps Assessment — Evidence Pack

These are the supplied screenshots renamed and ordered by the assessment evidence they demonstrate.

| File | Evidence |
|---|---|
| `evidence/01-jenkins-build-success-console.png` | Jenkins pipeline success console output (Build #5). |
| `evidence/02-jenkins-pipeline-stages.png` | Jenkins stage view showing checkout, lint/tests, image build and post actions. |
| `evidence/03-jenkins-job-overview.png` | Jenkins job overview/build history. |
| `evidence/04-deployed-image-tag.png` | Docker inspect showing the deployed versioned image tag. |
| `evidence/05-compose-services-healthy.png` | Docker Compose services; API and database report healthy. |
| `evidence/06-api-health-endpoint.png` | GET /health returns healthy. |
| `evidence/07-api-readiness-endpoint.png` | GET /ready confirms database connected and ready. |
| `evidence/08-prometheus-metrics-endpoint.png` | GET /metrics returns Prometheus-format metrics, including API request metrics. |
| `evidence/09-rollback-to-previous-image.png` | Rollback command and previous image tag verification. |
| `evidence/10-restore-version-5-and-compose-health.png` | Restore version 5 and verify API/database health. |
| `evidence/11-intentional-test-failure.png` | Intentional failing pytest test exits non-zero (failure demonstration). |
| `evidence/12-jenkins-failure-gate-blocks-build.png` | Jenkins Build #10 fails on the intentional test and skips the image-build stage. |
| `evidence/13-jenkins-final-job-status-build-11.png` | Jenkins job page showing Build #11 as the latest successful build. |

## Evidence notes

- The success console and stage screenshots are from Build #5. The final job overview screenshot shows Build #11 as the latest successful build, but the supplied screenshots do not include Build #11's full console log. If the reviewer expects proof that Build #11 ran against the final `main` commit, capture its Console Output showing the checked-out branch/commit, test summary, image tag, and `Finished: SUCCESS`.
- The Jenkins failure-gate evidence is Build #10 and is intentionally expected to fail; it demonstrates that the application-image stage is skipped after tests fail.
- The pytest screenshot shows `1 failed, 8 deselected` for the intentionally failing test. The normal suite screenshot from the conversation showed `8 passed, 1 deselected`; it is not separately included here because no standalone screenshot file for that exact output was supplied. Capture it if required.
- No screenshot in this pack proves an actual Prometheus server was running or that alert notifications fired. The metrics endpoint and configuration files are separate evidence.
- Screenshots are evidence artifacts only; they do not replace the source code, configuration, runbook, failure-investigation report, or AI disclosure in the GitHub repository.
