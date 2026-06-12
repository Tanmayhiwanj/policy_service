pipeline {
agent any


parameters {
    string(
        name: 'BRANCH_NAME',
        defaultValue: 'main',
        description: 'Enter Git branch name'
    )
}

environment {
    AWS_DEFAULT_REGION = 'ap-south-1'
}

stages {

    stage('Checkout Branch') {
        steps {
            git branch: params.BRANCH_NAME,
                url: 'https://github.com/Tanmayhiwanj/policy_service.git'
        }
    }

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
        echo 'Deployment Successful'
    }

    failure {
        echo 'Deployment Failed'
    }
}


}
