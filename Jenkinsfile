pipeline {
    agent {
        docker {
            image 'python:3-stretch'
        }
    }
    stages {
        stage('Build') {
            steps {
                checkout scm
                sh 'pip install -r requirements.txt --user'
            }
        }
        stage('Test') {
            steps {
                sh 'python manage.py jenkins --enable-coverage'
            }
            post {
                always {
                    junit 'reports/junit.xml'
                }
            }
        }
    }
}
