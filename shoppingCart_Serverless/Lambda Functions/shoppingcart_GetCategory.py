import json
import boto3

dynamoDBClient = boto3.client("dynamodb")

def lambda_handler(event, context):
    try:
        type = event["type"]
        if type=="all":
            categories = GetAllCategory("Categories")
            return categories
        else:
            category = GetCategoryById("Categories",str(type))
            return category
    except:
        return []
        

def GetAllCategory(tableName):
    response = dynamoDBClient.scan(TableName=tableName)
    return response["Items"]
    
def GetCategoryById(tableName,categoryId):
    response = dynamoDBClient.get_item(TableName=tableName,Key={"CategoryId":{'S':categoryId}})
    return [response["Item"]]