import json
import boto3
import uuid

dynamoDBClient = boto3.client("dynamodb")

def lambda_handler(event,context):

    newProduct = {
        "productId":{
            'S':str(uuid.uuid4())
        },
        "categoryId":{
            'S':event["categoryId"]
        },
        "product":{
            'S':event["product"]
        },     
        "price":{
            'S':event["price"]
        },
        "description":{
            'S':event["description"]
        },
        "stock":{
            'N':event["stock"]
        }
    }
    try:
        response = NewProduct('Prodcuts',newProduct)
    except:
        # Return HTTP code 000 is any error occure
        response = {"ResponseMetadata":{"HTTPStatusCode":000}}
    
    #Return response to API
    return {
        "StatusCode":response["ResponseMetadata"]["HTTPStatusCode"]
    }

# Add ne product to dynamoDB
def NewProduct(tablename,product):
    response = dynamoDBClient.put_item(TableName=tablename,Item=product)
    return response