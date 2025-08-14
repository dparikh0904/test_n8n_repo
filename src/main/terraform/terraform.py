Certainly! Below is a complete Terraform script that configures the AWS provider to deploy resources in AWS account `664091862099` by assuming the role `terraform_deploy_role`. It uses the `eu-west-2` region and stores the Terraform state in the S3 bucket `terraform-scripts-deployment-664091862099`.

This example deploys a simple EC2 instance running Ubuntu 22.04 LTS as the application. You can customize the resource section to fit your actual application.

---

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "terraform-scripts-deployment-664091862099"
    key    = "app/terraform.tfstate"
    region = "eu-west-2"
    encrypt = true
    # Uncomment below if you have DynamoDB locking
    # dynamodb_table = "terraform-locks"
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

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "app" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"

  tags = {
    Name = "TerraformDeployedApp"
  }
}
```

---

### How to use:

1. Make sure the S3 bucket `terraform-scripts-deployment-664091862099` exists in the `eu-west-2` region.

2. Your AWS credentials must have permission to assume the role `terraform_deploy_role` in account `664091862099`.

3. Initialize Terraform:

```bash
terraform init
```

4. Preview changes:

```bash
terraform plan
```

5. Deploy:

```bash
terraform apply
```

---

If you want a specific type of application deployment (like ECS, Lambda, RDS, or EKS), let me know!