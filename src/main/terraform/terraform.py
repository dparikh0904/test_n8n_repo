Certainly! Below is a sample Terraform configuration that deploys an example application (an EC2 instance as a simple placeholder) into AWS account `664091862099`, assuming the `terraform_deploy_role` in that account, targeting the `eu-west-2` region, and using the S3 bucket `terraform-scripts-deployment-664091862099` for remote state storage.

---

### `main.tf`

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "terraform-scripts-deployment-664091862099"
    key    = "terraform.tfstate"
    region = "eu-west-2"
    encrypt = true
    # Uncomment and set below if you have a DynamoDB table for state locking
    # dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = "eu-west-2"

  # Assume the deployment role in the target account
  assume_role {
    role_arn = "arn:aws:iam::664091862099:role/terraform_deploy_role"
  }
}

# Example Application Deployment: EC2 Ubuntu instance
data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "app_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name = "TerraformDeployedAppServer"
  }
}
```

---

### Usage instructions:

1. **Pre-requisites**:

   - Ensure the S3 bucket `terraform-scripts-deployment-664091862099` exists in `eu-west-2`.
   - Ensure your credentials can assume the role `terraform_deploy_role` in AWS account `664091862099`.
   - Optionally, create a DynamoDB table for state locking and configure it in the backend.

2. **Initialize Terraform**:

```bash
terraform init
```

3. **Apply the configuration**:

```bash
terraform apply
```

---

### Notes:

- Replace the resource section to deploy your actual application instead of this example EC2 instance.
- If you want state locking, create and specify a DynamoDB table in the backend section.
- This basic example assumes you have the necessary permissions and trust relationship set up for the role assumption.

If you want me to generate a script for another kind of resource or application deployment (ECS, Lambda, EKS, etc.), please provide the details.