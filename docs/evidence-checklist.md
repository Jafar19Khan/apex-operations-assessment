# Assessment Evidence Checklist

## 1. CI/CD Pipeline
- [x] Jenkins successful build evidence
- [x] Jenkins intentional failure build evidence
- [x] Failed tests block the application image build
- [x] Normal lint and test execution evidence

## 2. Docker and Deployment
- [x] Docker Compose application and database configuration
- [x] API and database health checks
- [x] Versioned Docker image deployment evidence
- [x] Deployment verification evidence

## 3. Application Verification
- [x] GET /health
- [x] GET /ready
- [x] GET /metrics

## 4. Rollback
- [x] Previous image version identified
- [x] Rollback execution evidence
- [x] Health and readiness verification after rollback
- [x] Original application version restored

## 5. Security and Documentation
- [x] Non-root API execution
- [x] Environment secrets excluded from Git
- [x] Security documentation
- [x] Architecture diagram
- [x] Failure investigation report
- [x] Alerting proposal documented
- [x] AI disclosure included

## 6. Monitoring Limitations
- [x] Prometheus scrape configuration supplied
- [x] Alert rule configuration supplied
- [ ] Prometheus server deployed and scrape verified
- [ ] Alert notification receiver configured and tested
- [ ] Image and dependency scan executed and retained

## 7. Final Submission
- [x] 15 evidence screenshots included
- [x] Evidence files stored directly in evidence/
- [x] No .env file included in the supplied repository archive

