Since you’ve asked several times but haven’t provided details about the application resources to deploy, here’s a **complete Terraform setup** that assumes the given role, uses the specified backend, and includes a placeholder resource you can replace with your application.

---

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "terraform-scripts-deployment-664091862099"
    key    = "app/terraform.tfstate"
    region = "eu-west-2"
    encrypt = true

    # Uncomment and configure if you have DynamoDB state locking
    #dynamodb_table = "terraform-lock-table"
  }
}

provider "aws" {
  region = "eu-west-2"

  assume_role {
    role_arn     = "arn:aws:iam::664091862099:role/terraform_deploy_role"
    session_name = "terraform-session"
  }
}

# Example resource — replace with your actual resources

resource "aws_s3_bucket" "example" {
  bucket = "my-app-bucket-664091862099"
  acl    = "private"

  tags = {
    Environment = "production"
    ManagedBy   = "Terraform"
  }
}
```

---

### How to run

1. Make sure bucket `terraform-scripts-deployment-664091862099` exists.
2. You have proper permissions / credentials to assume `terraform_deploy_role`.
3. Run:

```bash
terraform init
terraform plan
terraform apply
```

---

If you want a full Terraform script for a specific application architecture, please share details about the resources you want to deploy (EC2, Lambda, RDS, etc.). Happy to help!