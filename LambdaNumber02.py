import json

def lambda_handler(event, context):
    callingAgentNumber = event['agentNumber']
    message = event['message']
    print('Agent', callingAgentNumber, 'says:', message)
   
    #todo: do ur own logic
   
    responseBody = {
        'agentNumber': 56789,
        'message': 'Lambda 2 recieved secret message successful. Over!'
    }
    return {
        'statusCode': 200,
        'body': json.dumps(responseBody)
    }
