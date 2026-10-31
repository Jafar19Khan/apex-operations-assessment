pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Lint and tests') {
            steps {
                sh '''
                    docker build --pull -f Dockerfile.ci -t apex-operations-ci:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Build application image') {
            steps {
                sh 'docker build -t apex-operations-api:${BUILD_NUMBER} .'
            }
        }
    }

    post {
        success {
            echo 'Lint, tests and application image build passed.'
        }
        failure {
            echo 'CI failed; do not release this build.'
        }
    }
}
