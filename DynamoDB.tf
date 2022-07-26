resource "aws_dynamodb_table" "user_table"{
    name="user_table"
    billing_mode = "PROVISIONED"
    read_capacity= "100"
    write_capacity= "100"
}
resource "aws_dynamodb_table" "hobby_table"{
    name="hobby_table"
    billing_mode = "PROVISIONED"
    read_capacity= "100"
    write_capacity= "100"
}
resource "aws_dynamodb_table" "attendance_table_user"{
    name="attendance_table_user"
    billing_mode = "PROVISIONED"
    read_capacity= "100"
    write_capacity= "100"
    hash_key = "user_id"
    range_key= "date" 
    attribute {
    name = "user_id"
    type = "S"
  }
  attribute {
    name = "date"
    type = "S"
  }
}

