import json
import os

def lambda_handler(request, context):
    # validation
    if not 'photos' in request:
        raise Exception('photos needs to be provided')
        
    if not 'email' in request:
        raise Exception('email is required')
        
    if len(request['photos']) <= 1:
        raise Exception('not enough photos selected')
    
    QUEUE_URL = os.getenv('QUEUE_URL')
    
    ## push request to queue
    
    return {
        'statusCode': 200,
        'body': "Your queue: {}".format(QUEUE_URL)
    }