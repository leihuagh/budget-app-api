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
                withPythonEnv('python') {
                    sh 'pip install -r requirements.txt --user'
                }
            }
        }
        stage('Test') {
            steps {
                withPythonEnv('python') {
                    sh 'python manage.py jenkins --enable-coverage'
                }
            }
            post {
                always {
                    junit 'reports/junit.xml'
                }
            }
        }
    }
}
