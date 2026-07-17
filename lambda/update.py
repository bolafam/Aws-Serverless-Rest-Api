import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Records")


def lambda_handler(event, context):

    body = json.loads(event.get("body", "{}"))

    table.update_item(
        Key={
            "id": body["id"]
        },
        UpdateExpression="SET #n = :name, email = :email",
        ExpressionAttributeNames={
            "#n": "name"
        },
        ExpressionAttributeValues={
            ":name": body["name"],
            ":email": body["email"]
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Record updated successfully"
        })
    }