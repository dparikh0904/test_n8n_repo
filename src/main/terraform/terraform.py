Since you keep requesting a Terraform script "that will deploy the application" but haven't shared what the application is, I'll provide a generalized reusable Terraform skeleton that:

- Assumes the role `terraform_deploy_role` in AWS account `664091862099`
- Uses `eu-west-2` as region
- Uses the S3 bucket `terraform-scripts-deployment-664091862099` for state backend
- Contains a placeholder resource block you can replace with your actual app infrastructure

---

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "terraform-scripts-deployment-664091862099"
    key    = "app/terraform.tfstate"
    region = "eu-west-2"
    encrypt = true
    # dynamodb_table = "terraform-lock-table"  # Optional: state locking
  }
}

provider "aws" {
  region = "eu-west-2"

  assume_role {
    role_arn     = "arn:aws:iam::664091862099:role/terraform_deploy_role"
    session_name = "terraform-session"
  }
}

# ===== Example placeholder resource =====
# Replace these resources with your actual application resources

resource "aws_s3_bucket" "app_bucket" {
  bucket = "my-app-bucket-664091862099"  # Use a unique bucket name here
  acl    = "private"

  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}
```

---

### How to deploy

1. Make sure bucket `terraform-scripts-deployment-664091862099` exists in eu-west-2.
2. Configure local AWS credentials to allow assuming role `terraform_deploy_role` in account 664091862099.
3. Run Terraform:

```bash
terraform init
terraform plan
terraform apply
```

---

### Next steps

Please provide details about your actual application resources (EC2, Lambda, ECS, RDS, etc.) if you want a customized Terraform script for your app.

---

If you want, I can help you build that out once you share more details!