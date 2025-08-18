Certainly! I'll provide a reusable Terraform script template that assumes the role `terraform_deploy_role` in AWS account `664091862099` in region `eu-west-2`, using `terraform-scripts-deployment-664091862099` as the S3 backend bucket for terraform state.

As you haven't specified the actual "application" details (whether it's Lambda, ECS, EC2, etc.), I will create a simple example resource: an S3 bucket named uniquely for this setup. You can replace or extend this with your real app configuration.

---

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "terraform-scripts-deployment-664091862099"
    key    = "application/terraform.tfstate"
    region = "eu-west-2"
    encrypt = true
    # Uncomment below if you use DynamoDB for state locking
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

resource "aws_s3_bucket" "app_bucket" {
  bucket = "example-app-bucket-664091862099-eu-west-2"
  acl    = "private"

  tags = {
    Name        = "ExampleAppBucket"
    Environment = "Production"
  }
}

output "bucket_name" {
  description = "The name of the deployed S3 bucket (application)"
  value       = aws_s3_bucket.app_bucket.bucket
}
```

---

### Usage

1. Make sure the S3 bucket `terraform-scripts-deployment-664091862099` exists in `eu-west-2` (for state storage).
2. Your local credentials or environment must be able to assume the role `terraform_deploy_role` in account `664091862099`.
3. Commands:

```bash
terraform init
terraform plan
terraform apply
```

This configuration will:

- Store terraform state in the specified S3 bucket under `application/terraform.tfstate`.
- Assume the deploy role in the AWS account.
- Deploy a sample S3 bucket (replaceable with your application).

---

If you provide your actual app details (e.g., ECS, EC2, Lambda, etc.), I can prepare a more focused Terraform script.