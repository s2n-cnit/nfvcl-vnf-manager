pipeline {
    agent none
    stages {
/*      stage('Test') {
          agent { dockerfile true }
            steps {
                sh 'echo HOLA'
            }
        }
*/
        stage('Build') {
            agent any
            steps {
                sh 'docker build .'
                sh 'echo PUBLISH'
            }
        }
    }
}
