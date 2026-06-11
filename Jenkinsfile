pipeline {
agent any


stages {

    stage('Package Lambda') {
        steps {
            bat 'powershell Compress-Archive -Path lambda_function.py -DestinationPath lambda.zip -Force'
        }
    }

    stage('Deploy Lambda') {
        steps {
            bat '''
            aws lambda update-function-code ^
            --region ap-south-1 ^
            --function-name policy-service ^
            --zip-file fileb://lambda.zip
            '''
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
