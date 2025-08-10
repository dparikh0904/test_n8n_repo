Certainly! Here's a straightforward **Terraform** configuration to deploy your application using:

- AWS account: `664091862099`
- Assume role: `terraform_deploy_role`
- Region: `eu-west-2`
- Terraform remote backend in `terraform-scripts-deployment-664091862099` S3 bucket

---

This example includes:

- Backend config for remote state
- AWS provider with `assume_role` block for cross-account deployment
- A simple example resource (S3 bucket) as placeholder for your application deployment

---

### Terraform configuration (single file, e.g., `main.tf`)

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket         = "terraform-scripts-deployment-664091862099"
    key            = "app/terraform.tfstate"       # change path as needed
    region         = "eu-west-2"
    encrypt        = true
    # dynamodb_table = "terraform-lock-table"     # Optional: uncomment if you have locking table
  }
}

provider "aws" {
  region = "eu-west-2"

  assume_role {
    role_arn     = "arn:aws:iam::664091862099:role/terraform_deploy_role"
    session_name = "terraform-session"
  }
}

# Example resource to deploy your application - replace with your actual resources
resource "aws_s3_bucket" "app_bucket" {
  bucket = "example-app-bucket-664091862099-unique"  # modify to suit naming rules
  acl    = "private"

  tags = {
    Environment = "Production"
    ManagedBy   = "Terraform"
  }
}
```

---

### Instructions:

1. **Ensure the S3 bucket `terraform-scripts-deployment-664091862099` exists in `eu-west-2`.**

2. **(Optional)** If you want state locking, create a DynamoDB table (e.g., `terraform-lock-table`) and uncomment the `dynamodb_table` line.

3. **Run Terraform:**

```bash
terraform init
terraform plan
terraform apply
```

---

If you want me to tailor this further with your exact app resources (EC2, ECS, Lambda, etc.), please share those details!