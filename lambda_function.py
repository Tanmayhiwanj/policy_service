import json
import os
import pg8000

def lambda_handler(event, context):

    policy_no = event["queryStringParameters"]["policy_no"]

    conn = pg8000.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        port=int(os.environ["DB_PORT"])
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT policy_no, customer_name, status FROM policy WHERE policy_no=%s",
        (policy_no,)
    )

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "policy_no": row[0],
            "customer_name": row[1],
            "status": row[2]
        })
    }