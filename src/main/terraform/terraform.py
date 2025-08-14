Certainly! Here is a concise Terraform script that sets up AWS provider to deploy resources in the AWS account `664091862099` by assuming the role `terraform_deploy_role` using the `eu-west-2` region, and configures the S3 backend with bucket `terraform-scripts-deployment-664091862099`.

Below, I deploy a sample EC2 instance with Ubuntu 22.04 LTS as the example application. Adjust the application resources to your actual needs.

---

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "terraform-scripts-deployment-664091862099"
    key    = "app-deployment/terraform.tfstate"
    region = "eu-west-2"
    encrypt = true
    # dynamodb_table = "terraform-locks"  # optional for locking, if setup
  }
}

provider "aws" {
  region = "eu-west-2"

  assume_role {
    role_arn = "arn:aws:iam::664091862099:role/terraform_deploy_role"
  }
}

data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"]
}

resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name = "ExampleAppInstance"
  }
}
```

---

### Steps to Deploy

1. Ensure the S3 bucket `terraform-scripts-deployment-664091862099` exists in `eu-west-2`.
2. Ensure your AWS credentials can assume the given `terraform_deploy_role`.
3. Initialize Terraform:

   ```bash
   terraform init
   ```

4. Plan and apply:

   ```bash
   terraform apply
   ```

---

If you want me to generate a configuration for a specific kind of app (ECS, Lambda, EKS, RDS, etc.), just let me know!