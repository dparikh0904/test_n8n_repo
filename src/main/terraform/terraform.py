Certainly! Below is a clear, minimal Terraform script that assumes the role `terraform_deploy_role` in AWS account `664091862099`, uses the `eu-west-2` region, stores state in the S3 bucket `terraform-scripts-deployment-664091862099`, and deploys a simple example resource as a placeholder (you can customize it for your actual app).

---

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "terraform-scripts-deployment-664091862099"
    key    = "application/terraform.tfstate"
    region = "eu-west-2"
    encrypt = true
    # Uncomment and configure if using DynamoDB locking
    # dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = "eu-west-2"

  assume_role {
    role_arn     = "arn:aws:iam::664091862099:role/terraform_deploy_role"
    session_name = "tf-session"
  }
}

resource "aws_s3_bucket" "application_bucket" {
  bucket = "application-bucket-664091862099-eu-west-2"
  acl    = "private"

  tags = {
    Environment = "prod"
    ManagedBy   = "Terraform"
  }
}

output "bucket_name" {
  description = "Name of the deployed S3 bucket"
  value       = aws_s3_bucket.application_bucket.id
}
```

---

### Instructions:

1. Confirm the backend bucket `terraform-scripts-deployment-664091862099` exists in region `eu-west-2`.
2. Make sure the role `terraform_deploy_role` exists in AWS account `664091862099` and your credentials allow you to assume it.
3. Run:
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```
4. You'll get an output of the deployed bucket name.

---

If you want a Terraform script to deploy a specific type of AWS resource (like ECS, Lambda, RDS, etc.), please provide details!