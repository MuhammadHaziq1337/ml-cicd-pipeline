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
                   subject: "CI/CD Pipeline: Build #${BUILD_NUMBER} - Successfully Deployed",
                   body: """
                   <p>The deployment to production was successful.</p>
                   <p><b>Details:</b></p>
                   <ul>
                       <li>Build Number: ${BUILD_NUMBER}</li>
                       <li>Docker Image: muhammadhaziq123/ml-cicd-pipeline:${BUILD_NUMBER}</li>
                       <li>Status: SUCCESS</li>
                   </ul>
                   <p>The Docker image has been successfully built and pushed to Docker Hub.</p>
                   """,
                   mimeType: 'text/html',
                   to: 'haziqijaz12345@gmail.com',
                   from: 'jenkins@example.com',
                replyTo: 'jenkins@example.com'
               )
           }
       }
   }
}