provider "aws" {
  region  = "ap-northeast-1"
}

terraform {
  backend "s3" {
    bucket = "kinikare-terraform-management"
    region = "ap-northeast-1"
    key = "terraform.tfstate"
  }
}