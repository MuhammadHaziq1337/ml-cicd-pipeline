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
        // First log in to Docker Hub
        withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
            // Create a temp file with the password to avoid command line issues
            bat 'echo %DOCKER_PASSWORD%> temp.txt'
            bat 'type temp.txt | docker login -u %DOCKER_USERNAME% --password-stdin'
            bat 'del temp.txt'
            
            // Then push the image
            bat 'docker push muhammadhaziq123/ml-cicd-pipeline:%BUILD_NUMBER%'
        }
    }
}
        
        stage('Email Notification') {
            steps {
                emailext (
                    subject: "Pipeline: ${currentBuild.fullDisplayName} - Success",
                    body: "The deployment to production was successful. Docker image tag: ${BUILD_NUMBER}",
                    to: 'haziqijaz12345@gmail.com'
                )
            }
        }
    }
}