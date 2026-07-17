import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Records")


def lambda_handler(event, context):

    body = json.loads(event.get("body", "{}"))

    table.delete_item(
        Key={
            "id": body["id"]
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Record deleted successfully"
        })
    }