pipeline {
agent any


parameters {
    string(name: 'BRANCH_NAME', defaultValue: 'main')
}

stages {

    stage('Package Lambda') {
        steps {
            bat 'dir'
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


}
