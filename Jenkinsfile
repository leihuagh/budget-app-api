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
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
            // post {
            //     always {
            //         junit 'test-reports/results.xml'
            //     }
            // }
        }
    }
}
