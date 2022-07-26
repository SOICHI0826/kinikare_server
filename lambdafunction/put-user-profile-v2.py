import json
import jwt
import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
user_table    = dynamodb.Table('user_table')
hobby_table = dynamodb.Table('hobby_table')

def get_hobby_id(hobby):
    options = {
        'FilterExpression': Attr('hobby').contains(hobby),
    }
    response = hobby_table.scan(**options)
    return response['Items'][0]['hobby_id']

def lambda_handler(event,context):
    token = event['headers']['Authorization'] #ヘッダのトークン取得
    headers = jwt.get_unverified_header(token) 
    decoded_payload = jwt.decode(token, options={"verify_signature": False})
    
    # print("headers", headers)
    # print("payload", decoded_payload)
    # print("username", decoded_payload['cognito:username'])
    
    body = json.loads(event['body'])
    
    # hobbyのidを参照して、文字データを数字に変換して返す
    # hobbies_id_listの型は数値セット
    hobbies_id_list = set()
    for hobby in body['hobbies_list']:
        hobbies_id_list.add(get_hobby_id(hobby))
    print("pathからのuser_id", event['pathParameters']['user_id'])
    print("tokenからのuser_id", decoded_payload['cognito:username'])
    print("bodyからのuser_id", body['user_id'])
    if (event['pathParameters']['user_id'] == decoded_payload['cognito:username'] and event['pathParameters']['user_id'] == body['user_id'] ):
      user = user_table.put_item(
          Item = {
              'user_id': event['pathParameters']['user_id'],
              'birthplace': body['birthplace'],
              'comment': body['comment'],
              'default_office': body['default_office'],
              'department': body['department'],
              'first_name': body['first_name'],
              'first_name_kana': body['first_name_kana'],
              'gender': body['gender'],
              'hobbies_list': hobbies_id_list,
              'last_name': body['last_name'],
              'last_name_kana': body['last_name_kana']
          }
          )
      print("Successfully updated!")
      return {
        'statusCode': 204, #  403: forbidden
        'isBase64Encoded': False,
        'headers' : {
                "content-type": "application/json", #Lambdaプロキシ統合の使用を有効にした場合に必要となるCORS有効化の設定
                "Access-Control-Allow-Origin": "*"
                }
     }
    else:
      print("Failure!")
      return {
        'statusCode': 403, #  403: forbidden
        'isBase64Encoded': False,
        'headers' : {
                "content-type": "application/json", #Lambdaプロキシ統合の使用を有効にした場合に必要となるCORS有効化の設定
                "Access-Control-Allow-Origin": "*"
                }
     }

    # return {
    #     'statusCode': 204, #  403: forbidden
    #     'isBase64Encoded': False,
    #     'headers' : {
    #             "content-type": "application/json", #Lambdaプロキシ統合の使用を有効にした場合に必要となるCORS有効化の設定
    #             "Access-Control-Allow-Origin": "*"
    #             }
    #  }
