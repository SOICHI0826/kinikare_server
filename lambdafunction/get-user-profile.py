import boto3
import json
from decimal import Decimal
 
dynamodb = boto3.resource('dynamodb')
user_table    = dynamodb.Table('user_table')
hobby_table = dynamodb.Table('hobby_table')
 
def get_user(id):
    response = user_table.get_item(
            Key={
    
                 'user_id': id
            }
        )
    return response['Item']
    
def get_hobby(id):
    response = hobby_table.get_item(
            Key={
                'hobby_id': id
            }
        )
    return response['Item']

def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError
         
# TODO: event['user_id']の中に何も入ってない
def lambda_handler(event, context):
    # print(event['user_id'])
    print(event['pathParameters'])
    user = get_user(event['pathParameters']['user_id'])

    user['hobbies_list'] = list(user['hobbies_list'])
    
    hobbies_list = []
    for id in user['hobbies_list']:
        hobbies_list.append(get_hobby(id)['hobby'])
    
    user['hobbies_list'] = hobbies_list
    
    return {
        'statusCode': 200,
        'body': json.dumps(user, default=decimal_default_proc),
        'isBase64Encoded': False,
        'headers' : {"content-type": "application/json",
        "Access-Control-Allow-Origin": "*"}
        }
        
    