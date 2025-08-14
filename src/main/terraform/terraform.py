Certainly! Here's a Terraform script that:

- Configures the AWS provider to deploy in account `664091862099` by assuming the `terraform_deploy_role`
- Uses the `eu-west-2` region
- Uses S3 bucket `terraform-scripts-deployment-664091862099` for Terraform state backend
- Deploys a simple EC2 Ubuntu 22.04 instance as the example "application"

---

```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "terraform-scripts-deployment-664091862099"
    key    = "app/terraform.tfstate"
    region = "eu-west-2"
    encrypt = true
    # dynamodb_table = "terraform-locks"  # Uncomment and configure if you want state locking
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

  owners = ["099720109477"]  # Canonical
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

### Setup instructions

1. Make sure the S3 bucket `terraform-scripts-deployment-664091862099` exists in `eu-west-2`.
2. Ensure your current AWS CLI or environment credentials have permission to assume the `terraform_deploy_role` in account `664091862099`.
3. Run the Terraform commands:

```bash
terraform init
terraform apply
```

---

If you want me to create a script for a more complex app or service (ECS, Lambda, RDS, etc.), just let me know!