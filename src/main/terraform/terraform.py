Certainly! Here is a basic Terraform script that assumes the role `terraform_deploy_role` in AWS account `664091862099`, targets the `eu-west-2` region, and uses the S3 bucket `terraform-scripts-deployment-664091862099` for remote state.

You will need to replace the `application` resource section with your actual application's Terraform resources.

---

### `main.tf`

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket  = "terraform-scripts-deployment-664091862099"
    key     = "app/terraform.tfstate"
    region  = "eu-west-2"
    encrypt = true
    # dynamodb_table = "terraform-lock-table" # optionally, add for state locking
  }
}

provider "aws" {
  region = "eu-west-2"

  assume_role {
    role_arn     = "arn:aws:iam::664091862099:role/terraform_deploy_role"
    session_name = "terraform-session"
  }
}

# Example application resource (replace with your own)
resource "aws_s3_bucket" "app_bucket" {
  bucket = "app-bucket-664091862099-unique"   # Use your naming convention
  acl    = "private"

  tags = {
    Environment = "Production"
    ManagedBy   = "Terraform"
  }
}
```

---

### How to use

1. Make sure you have credentials configured locally that allow you to assume `terraform_deploy_role` in the target account.
2. The bucket `terraform-scripts-deployment-664091862099` must exist in `eu-west-2` for the Terraform backend.
3. Run:

```bash
terraform init
terraform plan
terraform apply
```

---

If you provide details about the application (like EC2, Lambda, RDS, ECS, etc.), I can help generate a more tailored Terraform script.