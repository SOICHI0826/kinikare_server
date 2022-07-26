resource "aws_lambda_function" "get-user-profile" {
    filename="lambdafunction/get-user-profile.py"
    function_name="get-user-profile" 
    # role=aws_iam_role.iam_for_lambda.arn
    role="arn:aws:iam::316324343548:role/lambda-role-kinikare"
    handler="lambda_function.lambda_handler"
    runtime="python3.9" 
}

resource "aws_lambda_function" "put-user-profile-v2" {
    filename="lambdafunction/put-userp-rofilev-2.py"
    function_name="put-userp-rofilev-2"
    # role=aws_iam_role.iam_for_lambda.arn
    role="arn:aws:iam::316324343548:role/service-role/put-user-profile-role-mcrvos6j"
    handler="lambda_function.lambda_handler"
    runtime="python3.8"
    layers= [
          "arn:aws:lambda:ap-northeast-1:316324343548:layer:jwt:2",
        ]
}

resource "aws_lambda_function" "getHobby" {
    filename="lambdafunction/getHobby.py"
    function_name="getHobby"
    # role=aws_iam_role.iam_for_lambda.arn
    role="arn:aws:iam::316324343548:role/lambda-role-kinikare"
    handler="lambda_function.lambda_handler"
    runtime="python3.9" 
}

resource "aws_lambda_function" "get_attendance" {
    filename="lambdafunction/get_attendance.py"
    function_name="get_attendance"
    # role=aws_iam_role.iam_for_lambda.arn
    role="arn:aws:iam::316324343548:role/lambda-role-kinikare"
    handler="lambda_function.lambda_handler"
    runtime="python3.9" 
}

resource "aws_lambda_layer_version" "lambda_layer" {
  filename   = "lambdafunction/layer.zip"
  layer_name = "jwt"
  compatible_architectures = ["x86_64"]

  compatible_runtimes = ["python3.8"]
}

#import command
#terraform import aws_lambda_function.(インポート先の名前) (インポートしたいlambda関数の名前)