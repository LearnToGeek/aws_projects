import boto3

dynamoDBClient = boto3.client("dynamodb")

def NewCategory(tableName,category):
    response = dynamoDBClient.put_item(TableName=tableName,Item=category)
    return response