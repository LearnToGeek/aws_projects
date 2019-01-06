import json
import datetime
import uuid
import boto3

dynamoDBClient = boto3.client("dynamodb")


def lambda_handler(event, context):
    
    newCategory = {
        "CategoryId":{
          'S':str(uuid.uuid4())
        },
        "Category":{
            'S':event["Category"]
        },
        "Description":{
            'S':event["Description"]
        },
        "CreatedOn":{
            'S':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
    }
    
    response = NewCategory("Categories",newCategory)
    print("Category Saved !")
    return {
       'body':json.dumps(response)
    }

def NewCategory(tableName,category):
    response = dynamoDBClient.put_item(TableName=tableName,Item=category)
    return response