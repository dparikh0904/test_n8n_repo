Certainly! Below is a Terraform configuration tailored to deploy an application into AWS account `664091862099`, by assuming the `terraform_deploy_role` role in that account, targeting the `eu-west-2` region, and using the S3 bucket `terraform-scripts-deployment-664091862099` as the remote state backend.

---

### Assumptions & Prerequisites

- Your local AWS CLI (or environment) has permissions to assume the IAM role `terraform_deploy_role` in the target account `664091862099`.
- The S3 bucket `terraform-scripts-deployment-664091862099` exists in `eu-west-2` for Terraform state storage.
- (Optionally) a DynamoDB lock table (e.g., `terraform-lock-table`) exists in the account and region to prevent concurrent state modifications.
- The application definition here is minimal (simple S3 bucket example). Replace or extend resources to match your actual application.

---

### Example: Terraform Script

**File: `main.tf`**

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket         = "terraform-scripts-deployment-664091862099"
    key            = "app/terraform.tfstate"
    region         = "eu-west-2"
    encrypt        = true
    dynamodb_table = "terraform-lock-table" # Optional locking table, omit if unused
  }
}

provider "aws" {
  region = "eu-west-2"

  assume_role {
    role_arn     = "arn:aws:iam::664091862099:role/terraform_deploy_role"
    session_name = "terraform-session"
  }
}

# Example resource: S3 bucket for the application
resource "aws_s3_bucket" "app_bucket" {
  bucket = "example-app-bucket-664091862099"
  acl    = "private"

  tags = {
    Environment = "Production"
    ManagedBy   = "Terraform"
  }
}

# Add your application resources below this line
# e.g., aws_ec2_instance, aws_lambda_function, aws_rds_instance, etc.
```

---

### Steps to Use

1. **Prepare your environment**

Make sure you have AWS CLI configured with credentials that can assume `terraform_deploy_role` in account `664091862099`.

2. **Initialize Terraform**

```bash
terraform init
```

3. **Plan the deployment**

```bash
terraform plan
```

4. **Apply the deployment**

```bash
terraform apply
```

---

### Notes

- Replace the example S3 bucket resource with your actual application resources.
- Adjust the backend key (here `"app/terraform.tfstate"`) as appropriate, maybe reflecting your environment or app.
- If you do not have a DynamoDB table for state locking, you can remove the `dynamodb_table` line from the backend configuration.
- Ensure the role `terraform_deploy_role` has enough permissions in the target AWS account to create/manipulate the necessary resources.

---

If you want me to generate a more detailed example based on your actual application (e.g., EC2, Lambda, ECS, RDS), feel free to provide details!