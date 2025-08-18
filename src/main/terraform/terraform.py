Certainly! Here's a complete and reusable Terraform script snippet tailored to your exact requirements:

- Target AWS Account ID: **664091862099**
- Assume Role: **terraform_deploy_role**
- AWS Region: **eu-west-2**
- Backend S3 bucket for state: **terraform-scripts-deployment-664091862099**
- Simple example resource deployed under that account (replace with your real app resources)

---

### `main.tf`

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "terraform-scripts-deployment-664091862099"
    key    = "application/terraform.tfstate"
    region = "eu-west-2"
    encrypt = true
    # Uncomment below if you have a DynamoDB table for state locking
    # dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = "eu-west-2"

  assume_role {
    role_arn     = "arn:aws:iam::664091862099:role/terraform_deploy_role"
    session_name = "terraform-session"
  }
}

# Replace this resource with your application resources
resource "aws_s3_bucket" "app_bucket" {
  bucket = "my-app-bucket-664091862099-eu-west-2"
  acl    = "private"

  tags = {
    Project     = "MyApp"
    Environment = "Production"
  }
}

output "app_bucket_name" {
  value       = aws_s3_bucket.app_bucket.bucket
  description = "The name of the deployed application S3 bucket"
}
```

---

### How to use:

1. Create the S3 bucket `terraform-scripts-deployment-664091862099` in the AWS account/region you use for state.
2. Confirm that the role `terraform_deploy_role` exists in account `664091862099`, and your user/role can assume it.
3. Run locally or in your CI/CD environment:

```bash
terraform init
terraform plan
terraform apply
```

This will assume the role, deploy the S3 bucket, and store state in the backend bucket.

---

If you want a specific application deployed (ECS, Lambda, etc.), please share details!