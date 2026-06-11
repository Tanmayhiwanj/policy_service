pipeline {
agent any


environment {
    AWS_DEFAULT_REGION = 'ap-south-1'
}

stages {

    stage('Package Lambda') {
        steps {
            bat 'powershell Compress-Archive -Path lambda_function.py -DestinationPath lambda.zip -Force'
        }
    }

    stage('Deploy Lambda') {
        steps {
            withCredentials([
                [$class: 'AmazonWebServicesCredentialsBinding',
                 credentialsId: 'aws-creds']
            ]) {
                bat '''
                aws lambda update-function-code ^
                --region ap-south-1 ^
                --function-name policy-service ^
                --zip-file fileb://lambda.zip
                '''
            }
        }
    }
}

post {
    success {
        echo 'Lambda deployment successful'
    }

    failure {
        echo 'Lambda deployment failed'
    }
}


}
