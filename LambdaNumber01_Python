import json
import boto3

lambdaClient = boto3.client('lambda')

def lambda_handler(event, context):
    input = {
       'agentnumber' : 12345,
       'message': 'A secret message from lambda number 1. Over!!'
    }
   
    response = lambdaClient.invoke(
       FunctionName='arn:aws:lambda:us-east-1:933135655749:function:LambdaNumberTwo',
       InvocationType='RequestResponse',
       Payload=json.dumps(input)
       )
       
    responsePayload = json.load(response['Payload'])
    print(responsePayload)
   
    return {
        'statusCode': 200,
        'message': 'Succes'
    }
