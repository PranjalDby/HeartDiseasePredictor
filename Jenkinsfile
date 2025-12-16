pipeline {
    agent any

    environment {
        IMAGE_NAME = "pranjaldby/heart_disease_pred"
        CONTAINER_NAME = "heart_disease_pred"
    }

    stages {

        stage('Checkout Source Code') {
            steps {
                git branch: 'main',
                    url:'https://github.com/PranjalDby/HeartDiseasePredictor.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t heart_disease_predictor .
                '''
            }
        }
        
        stage('Deploy Container') {
            steps {
                echo 'Deploying container...'
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true

                    docker run -d \
                      --name ${CONTAINER_NAME} \
                      -p 8080:8080 \
                      ${IMAGE_NAME}:${BUILD_NUMBER}
                """
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
