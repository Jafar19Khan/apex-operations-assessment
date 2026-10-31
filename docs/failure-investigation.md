# Failure Investigation Report

## Incident
Jenkins CI pipeline failure during the intentional failure-gate demonstration.

## Environment
- Project: Apex Operations DevOps Assessment
- CI tool: Jenkins
- Demonstration build: Build #10
- Pipeline: apex-operations

## Observed Symptoms
- The test stage returned a non-zero exit code.
- Jenkins reported one failed test.
- The application image build stage was skipped.
- The pipeline finished with FAILURE.

## Root Cause
The test `test_intentional_failure_demo` was deliberately executed to verify that Jenkins blocks subsequent pipeline stages when tests fail.

The assertion intentionally compared different expected and actual values:
- Expected: `expected failure`
- Actual: `passing test`

This caused pytest to return a non-zero exit code.

## Impact
The application image build stage did not execute. This demonstrated that a failed test prevents the pipeline from proceeding to the next stage.

## Resolution
The intentional failure was removed from the normal CI execution path. The regular test command was restored.

The subsequent successful Jenkins build (#11) demonstrated that the normal pipeline could complete successfully.

## Preventive Controls
- Keep intentional failure demonstrations separate from normal release builds.
- Run linting and automated tests before building the release image.
- Do not release an image when the CI pipeline fails.
- Review Jenkins console output when investigating pipeline failures.

## Verification
- Build #10: Expected FAILURE during intentional failure-gate test.
- Build #11: SUCCESS after restoring the normal test command.

## Conclusion
The demonstrated failure was intentional and not an unresolved application defect. Jenkins correctly prevented the application image build after the test command failed.
