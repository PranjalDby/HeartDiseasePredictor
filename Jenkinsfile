pipeline {
    agent any

    environment {
        IMAGE_NAME = "heart_disease_predictor"
        CONTAINER_NAME = "heart_disease_predictor"
        PORT = "8080"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh """
                docker build -t ${IMAGE_NAME}:latest .
                """
            }
        }

        stage('Deploy Container') {
            steps {
                echo "Deploying container..."
                sh """
                # Stop old container if exists
                if [ \$(docker ps -aq -f name=${CONTAINER_NAME}) ]; then
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                fi

                # Run new container
                docker run -d \
                    -p ${PORT}:5050 \
                    --name ${CONTAINER_NAME} \
                    ${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed — check logs."
        }
        always {
            echo "Cleaning up workspace..."
            cleanWs()
        }
    }
}
