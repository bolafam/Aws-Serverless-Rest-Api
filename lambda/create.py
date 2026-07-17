import json
import uuid
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Records")


def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))

    item = {
        "id": str(uuid.uuid4()),
        "name": body.get("name"),
        "email": body.get("email")
    }

    table.put_item(Item=item)

    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "Record created successfully",
            "data": item
        })
    }