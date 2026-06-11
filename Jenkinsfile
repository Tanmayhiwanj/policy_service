pipeline {
agent any


parameters {
    string(
        name: 'LAMBDA_NAME',
        defaultValue: 'policy-service',
        description: 'AWS Lambda Name'
    )
}

stages {

    stage('Package') {
        steps {
            bat 'powershell Compress-Archive -Path lambda_function.py -DestinationPath lambda.zip -Force'
        }
    }

    stage('Deploy') {
        steps {
            withCredentials([
                [$class: 'AmazonWebServicesCredentialsBinding',
                 credentialsId: 'aws-creds']
            ]) {

                bat """
                aws lambda update-function-code ^
                --region ap-south-1 ^
                --function-name %LAMBDA_NAME% ^
                --zip-file fileb://lambda.zip
                """
            }
        }
    }
}

}
