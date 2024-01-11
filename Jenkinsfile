pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        sh 'docker build -t everlong-app .'
        sh 'docker tag everlong-app $DOCKER_BFLASK_IMAGE'
      }
    }
    stage('Test') {
      steps {
        sh 'docker run -v /var/lib/jenkins/workspace/everlong_pipeline:/flask_app everlong-app python -m unittest discover -s /flask_app -p "tests.py"'
      }
    }
    stage('Deploy') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKER_REGISTRY_CREDS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
          sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin docker.io"
          sh 'docker push $DOCKER_BFLASK_IMAGE'
        }
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}
