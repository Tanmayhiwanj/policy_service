import json
import requests


def lambda_handler(event, context):

    policy_no = event["pathParameters"]["policy_no"]

    response = requests.get(
        f"https://policy-api.company.com/policy/{policy_no}",
        timeout=30
    )

    policy_data = response.json()

    return {
        "statusCode": 200,
        "body": json.dumps(policy_data)
    }