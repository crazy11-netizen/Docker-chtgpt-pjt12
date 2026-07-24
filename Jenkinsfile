pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Environment Check') {
            steps {
                sh '''
                    echo "===== Jenkins Environment ====="
                    whoami
                    pwd
                    docker --version
                    docker compose version
                    git --version
                '''
            }
        }

        stage('Build Info') {
            steps {
                sh '''
                    echo "===== Build Metadata ====="
                    echo "Build Number: ${BUILD_NUMBER}"
                    echo "Build ID: ${BUILD_ID}"
                    echo "Workspace: ${WORKSPACE}"
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker compose build'
            }
        }


	stage('Push Docker Image') {
    		steps {
        		withCredentials([usernamePassword(
            		credentialsId: 'dockerhub-creds',
           		usernameVariable: 'DOCKER_USER',
            		passwordVariable: 'DOCKER_PASS'
        	)]) {
            	sh '''
                	echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin

                	docker tag inventory-app:latest $DOCKER_USER/inventory-management:${BUILD_NUMBER}

                	docker tag inventory-app:latest $DOCKER_USER/inventory-management:latest

                	docker push $DOCKER_USER/inventory-management:${BUILD_NUMBER}

               		 docker push $DOCKER_USER/inventory-management:latest

                	docker logout
            '''
        }
    }
}


        stage('Stop Existing Containers') {
            steps {
                sh 'docker compose down --remove-orphans || true'
            }
        }

        stage('Start Application') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Initialize Database') {
            steps {
                // Wait for MySQL to finish booting, then seed the database schema/data
                sh 'sleep 10'
                sh 'docker exec -i inventory-mysql mysql -u inventory_user -pinventory_password inventory_db < ./database/init.sql || true'
            }
        }

        stage('Verify Images & Containers') {
            steps {
                sh '''
                    echo "===== Docker Images ====="
                    docker images

                    echo "===== Running Containers ====="
                    docker ps
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    echo "===== Application Health Check ====="
                    sleep 10
                    curl --fail http://localhost:5000 || (echo "Health check failed!" && exit 1)
                '''
            }
        }
    }

    post {
        always {
            sh '''
                echo "===== Cleaning Up Unused Docker Resources ====="
                docker image prune -f
                docker container prune -f
                docker builder prune -f
            '''
        }

        failure {
            sh '''
                echo "===== Pipeline Failed! Dumping Container Logs ====="
                docker compose logs
            '''
        }
    }
}
