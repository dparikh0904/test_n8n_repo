Certainly! Below is a clean, reusable **Terraform script** template that assumes the role `terraform_deploy_role` in AWS account `664091862099`, targets the `eu-west-2` region, and stores Terraform state in the S3 bucket `terraform-scripts-deployment-664091862099`. This template includes a placeholder example resource that you'll replace with your actual application resources.

---

### Terraform Script (e.g., `main.tf`)

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket         = "terraform-scripts-deployment-664091862099"
    key            = "application/terraform.tfstate"
    region         = "eu-west-2"
    encrypt        = true
    # dynamodb_table = "terraform-lock-table" # Optional: uncomment if you use DynamoDB for locking
  }
}

provider "aws" {
  region = "eu-west-2"

  assume_role {
    role_arn     = "arn:aws:iam::664091862099:role/terraform_deploy_role"
    session_name = "terraform-session"
  }
}

# ===== Replace this example resource block with your application's actual resources =====

resource "aws_s3_bucket" "example_app_bucket" {
  bucket = "example-app-bucket-664091862099" # Replace with unique bucket name
  acl    = "private"

  tags = {
    Environment = "Production"
    ManagedBy   = "Terraform"
  }
}
```

---

### How to use

1. Ensure your current AWS credentials can assume the role `terraform_deploy_role` in account `664091862099`.
2. The S3 bucket `terraform-scripts-deployment-664091862099` must exist in `eu-west-2` and be accessible.
3. **Initialize Terraform backend:**

```bash
terraform init
```

4. **Plan the deployment:**

```bash
terraform plan
```

5. **Apply changes:**

```bash
terraform apply
```

---

If you want me to generate a script to deploy a specific application resource (e.g., EC2 instance, Lambda, RDS, ECS service), please provide details of the application!