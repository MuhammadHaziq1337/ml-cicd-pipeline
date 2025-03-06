pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t muhammadhaziq123/ml-cicd-pipeline:%BUILD_NUMBER% .'
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-credentials', variable: 'DOCKER_HUB_PASSWORD')]) {
                    bat 'docker login -u muhammadhaziq123 -p %DOCKER_HUB_PASSWORD%'
                    bat 'docker push muhammadhaziq123/ml-cicd-pipeline:%BUILD_NUMBER%'
                }
            }
        }
        
        stage('Email Notification') {
            steps {
                emailext (
                    subject: "Pipeline: ${currentBuild.fullDisplayName} - Success",
                    body: "The deployment to production was successful. Docker image tag: ${BUILD_NUMBER}",
                    to: 'i212692@nu.edu.pk'
                )
            }
        }
    }
}