import boto3
import json
from decimal import Decimal


dynamodb = boto3.resource('dynamodb')
hobby_table = dynamodb.Table('hobby_table')

def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def lambda_handler(event, context):


  return {
    'body': json.dumps(hobby_table.scan(),default=decimal_default_proc),
    'statusCode': 200,
    'isBase64Encoded': False,
    'headers' : {
        "content-type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }
  }
  

