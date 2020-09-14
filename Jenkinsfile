def dockerImage

pipeline {
  environment {
    imagename = "opensourcemano/api-fe"
    registryCredential = '<credentials>'  // To be updated with actual ID in the future
  }
  agent any
  stages {
    stage('Build API-FE image') {
      steps{
        sh "echo Building API-FE image"
        script {
          dockerImage = docker.build "${env.imagename}:${env.BUILD_NUMBER}"
        }
      }
    }
    stage('Upload to Docker registry') {
      steps{
        sh "echo Here it would upload the image with appropriate tags: build number, latest"
        /*script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push("${env.BUILD_NUMBER}")
            dockerImage.push('latest')
          }
        }*/
      }
    }
    stage('Remove unused Docker image') {
      steps{
        sh "docker rmi ${imagename}:${BUILD_NUMBER}"
        // Commented until "upload" stage can be uncommented as well
        //sh "docker rmi ${imagename}:latest"
      }
    }
  }
}
