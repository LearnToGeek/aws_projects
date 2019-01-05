import json
import datetime
import uuid
import DBConnector as dbconnect


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
    
    response = dbconnect.NewCategory("Categories",newCategory)
    print("Category Saved !")
    return {
       'body':json.dumps(response)
    }