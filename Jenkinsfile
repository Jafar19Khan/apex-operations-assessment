pipeline {
    agent any
    options { timestamps(); disableConcurrentBuilds() }
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Lint and tests') {
            steps {
                sh '''docker run --rm -v "$WORKSPACE:/workspace" -w /workspace python:3.12-slim sh -c "pip install --no-cache-dir -r requirements.txt && ruff check app tests && python -m pytest -q"'''
            }
        }
        stage('Build image') {
            steps { sh 'docker build -t apex-operations-api:${BUILD_NUMBER} .' }
        }
    }
    post {
        success { echo 'Lint, tests and image build passed.' }
        failure { echo 'CI failed; do not release this build.' }
    }
}
