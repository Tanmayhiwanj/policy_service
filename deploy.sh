#!/bin/bash

zip -r lambda.zip lambda_function.py

aws lambda update-function-code \
    --function-name policy-service \
    --zip-file fileb://lambda.zip