import boto3
import base64

def get_img_from_s3(id):
    s3 = boto3.client('s3')
    bucket_name = 'profile-image-kinikare'
    file_path = id+'.png'
    responce = s3.get_object(Bucket=bucket_name, Key=file_path)
    body = responce['Body'].read()
    body = base64.b64encode(body).decode('utf-8')
    return body


def lambda_handler(event, context):
    # print("user_id", event['pathParameters']['user_id'])
    img = get_img_from_s3(event['pathParameters']['user_id'])
    
    return {
            'statusCode': 200,
            'body': img,
            'isBase64Encoded': True,
            'headers' : {"content-type": "image/png",
            "Access-Control-Allow-Origin": "*"}
            }
