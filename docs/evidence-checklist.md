# Assessment Evidence Checklist

## 1. CI/CD Pipeline
- [x] Jenkins successful build (#11)
- [x] Jenkins intentional failure build (#10)
- [x] Failed tests block the application image build

## 2. Docker and Deployment
- [x] Docker Compose application and database
- [x] API and database health checks
- [x] Versioned Docker image deployment
- [x] Deployment verification

## 3. Application Verification
- [x] GET /health
- [x] GET /ready
- [x] GET /metrics

## 4. Rollback
- [x] Previous image version identified
- [x] Rollback executed
- [x] Health and readiness verified after rollback
- [x] Original application version restored

## 5. Security and Documentation
- [x] Non-root API execution
- [x] Environment secrets excluded from Git
- [x] Security documentation
- [ ] Architecture diagram reviewed
- [ ] Failure investigation documented
- [ ] Alerting proposal documented
- [x] AI disclosure file included

## 6. Final Submission
- [ ] Required screenshots committed
- [ ] Final GitHub repository reviewed
- [ ] No .env file committed
