pipeline {
    agent any
    tools{
        maven 'maven_3.9'
    }
    stages{
        stage('Build Maven'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/SOURHEAD/everlong']]])
                sh 'mvn clean install'
            }
        }
        stage('Build docker image'){
            steps{
                script{
                    sh 'docker build -t Sourhead\everlong .'
                }
            }
        }
    }
}
