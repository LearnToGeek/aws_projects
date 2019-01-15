import json
import boto3
import datetime
import uuid

dynamoDBClient = boto3.client("dynamodb")


def lambda_handler(event, context):

    # New Category    
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
    try:
        response = NewCategory("Categories",newCategory)
    except:
        # Return Response with HTTP code 000
        response = {'ResponseMetadata':{'HTTPStatusCode':000}}

    # Retrun response to API     
    return {
       'StatusCode':response['ResponseMetadata']['HTTPStatusCode']
    }


# Method to add new category in DynamoDB
def NewCategory(tableName,category):
    response = dynamoDBClient.put_item(TableName=tableName,Item=category)
    return response