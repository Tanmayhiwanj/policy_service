pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/company/policy-service.git'
            }
        }

        stage('Package') {
            steps {
                sh 'zip lambda.zip lambda_function.py'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                aws lambda update-function-code \
                --function-name policy-service \
                --zip-file fileb://lambda.zip
                '''
            }
        }
    }
}