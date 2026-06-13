from config import ENV, DB_HOST, API_URL
from policy_service import get_policy

def lambda_handler(event, context):


policy_no = event.get("policy_no", "12345")

response = get_policy(policy_no)

return {
    "statusCode": 200,
    "environment": ENV,
    "db_host": DB_HOST,
    "api_url": API_URL,
    "data": response
}

