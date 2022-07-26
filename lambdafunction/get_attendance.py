import boto3
import json
from decimal import Decimal
from boto3.dynamodb.conditions import Key
 
dynamodb = boto3.resource('dynamodb')
attendance_table    = dynamodb.Table('attendance_table_user')
 
#queryで特定のuser_idの出社予定取ってくる
def query_attendance(id): 
    result = attendance_table.query(
        KeyConditionExpression=Key('user_id').eq(id)
    )
    return result['Items']
    
def decimal_default_proc(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError
         
def lambda_handler(event, context):
    attendance = query_attendance(event['pathParameters']['user_id'])
    # print("attendanceのリスト", attendance)
  
    return {
        'statusCode': 200,
        'body': json.dumps(attendance, default=decimal_default_proc),
        'isBase64Encoded': False,
        'headers' : {"content-type": "application/json",
        "Access-Control-Allow-Origin": "*"}
        }
        
    