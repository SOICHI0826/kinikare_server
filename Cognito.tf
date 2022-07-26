resource "aws_cognito_user_pool" "kinikare-user" {
        name="kinikare-user"
        auto_verified_attributes   = [
           "email"
        ]
        sms_authentication_message = " 認証コードは {####} です。"
        tags                       = {}
        account_recovery_setting {
          recovery_mechanism {
              name     = "verified_email"
              priority = 1
            }
          recovery_mechanism {
              name     = "verified_phone_number"
              priority = 2
            }
        }
        email_configuration {
          email_sending_account = "COGNITO_DEFAULT"
        }

        username_configuration {
          case_sensitive = true
        }
        password_policy {
          minimum_length                   = 8
          require_lowercase                = true
          require_numbers                  = true
          require_symbols                  = false
          require_uppercase                = true
          temporary_password_validity_days = 7
        }
}