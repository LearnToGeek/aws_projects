import boto3

def csv_read(event,context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    s3client = boto3.client('s3')
    data = s3client.get_object(Bucket=bucket, Key=key)
    rows = data['Body'].read().split('\n')
    
    dynamodbclient = boto3.resource('dynamodb')
    table_client = dynamodbclient.Table('friends')

    with table_client.batch_writer() as batch:
        for row in rows:
            batch.put_item({
                'id': row.split(',')[0],
                'Firstname': row.split(',')[1],
                'Lastname': row.split(',')[2],
                'Nikname': row.split(',')[3]
            })
    
    
    print('Your Lambda Function executed successfully..!!')