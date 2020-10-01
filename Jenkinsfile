def dockerImage

pipeline {
  environment {
    imagename = "opensourcemano/api-fe"
    registryCredential = 'dockerhub'
  }
  agent any
  stages {
    stage('Build API-FE image') {
      steps{
        echo "Building API-FE image"
        script {
          dockerImage = docker.build "${env.imagename}:${env.BUILD_NUMBER}"
        }
      }
    }
    stage('Upload to Docker registry') {
      steps{
        echo "Uploads the image with appropriate tags: build number, latest"
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push("${env.BUILD_NUMBER}")
            dockerImage.push('latest')
          }
        }
      }
    }
    stage('Remove unused Docker image') {
      steps{
        sh "docker rmi ${imagename}:${BUILD_NUMBER}"
        sh "docker rmi ${imagename}:latest"
      }
    }
  }
}
