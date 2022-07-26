# Kinikare_server

# Terraformで既存の構成を読み込むための手順

## 参考サイト

- Terraformの公式ドキュメント  
[Documentation | Terraform by HashiCorp](https://www.terraform.io/docs)

- TerraformのAWSの公式ドキュメント  
[Docs overview | hashicorp/aws | Terraform Registry](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

- [既存のAWS環境を後からTerraformでコード化する | DevelopersIO](https://dev.classmethod.jp/articles/aws-with-terraform/#toc-7)

---
---

## Terraformの理解

### provider.tfって何？

テラフォームの設定を書くために作る。
ファイル名には特に意味はなく、.tfファイルのどこかに以下のような構文で書かれていれば良いが、どこに書いたかわからなくなるのでファイルを作る。
```
provider "aws" {
  region  = "ap-northeast-1"
}
```

---

### tfファイルとterraform importコマンドの関係

#### 書き方

```
resource "＜リソースの種類＞" "＜リソースの名前＞" {
    
}
```

```zsh
% terraform import ＜リソースの種類＞.＜リソースの名前＞ ＜リソースの識別ID＞
```

＜リソースの識別ID＞が何に当たるかはインスタンスの種類による

- S3：バケット名
- Cognito User Pool：ユーザープールID

#### 例

```
resource "aws_s3_bucket" "kinikare-front-production" {
    
}
```

```zsh
% terraform import aws_s3_bucket.kinikare-front-production kinikare-front-production
```

---

### `% terraform plan`すると、簡単に「No Changes」になるけどいいのか

`import`した時点で、.tfファイルをどれくらい詳しく書いているかで、.tfstateの中身の詳しさも変わる。よって、.tfに最低限しか書かない状態で`import`していたら、planした時もほとんどデフォルトの設定が反映されて「No Changes」になりやすい。

---

### 特定のResourceに対してだけ`plan`する方法

```zsh
% terraform plan -target=＜リソース名（`import`したときの第一引数：hogehoge.fugafuga）＞
```

#### 例

```zsh
% terraform plan -target=aws_s3_bucket.kinikare-front-production
```

---
---

## 作業手順

1. Terraformやると

---
---

## 前田さんに聞きたいこと
