pipeline {
agent any

parameters {
    string(
        name: 'BRANCH_NAME',
        defaultValue: 'main',
        description: 'Enter Git Branch Name'
    )
}

environment {
    AWS_DEFAULT_REGION = 'ap-south-1'
}

stages {

    stage('Clean Workspace') {
        steps {
            deleteDir()
        }
    }

    stage('Checkout Branch') {
        steps {
            git branch: params.BRANCH_NAME,
                url: 'https://github.com/Tanmayhiwanj/policy_service.git'
        }
    }

    stage('Verify Branch') {
        steps {
            bat 'git branch'
            bat 'git log -1'
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
