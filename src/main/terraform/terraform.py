Certainly! Below is a complete example Terraform configuration to deploy an application into AWS account `664091862099` in the `eu-west-2` region, assuming the IAM role `terraform_deploy_role`, and using the S3 bucket `terraform-scripts-deployment-664091862099` for storing the Terraform state.

Since you didn't specify the application details, I will create an example deployment based on an ECS Fargate service running a simple Nginx container. This is a typical "application" deployment and you can modify it for your use case.

---

### Directory structure (example)
```
├── main.tf
├── variables.tf
├── outputs.tf
```

---

### `main.tf`
```hcl
terraform {
  required_version = ">= 1.0"

  backend "s3" {
    bucket = "terraform-scripts-deployment-664091862099"
    key    = "app/terraform.tfstate"
    region = "eu-west-2"
    encrypt = true
    # Uncomment the next line if you have a DynamoDB table for state locking
    # dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = "eu-west-2"

  assume_role {
    role_arn     = "arn:aws:iam::664091862099:role/terraform_deploy_role"
    session_name = "terraform-session"
  }
}

# VPC Data Source (you can specify your own VPC ID if needed)
data "aws_vpc" "default" {
  default = true
}

# Subnets (private or public, here using default VPC public subnets)
data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }

  filter {
    name   = "default-for-az"
    values = ["true"]
  }
}

# ECS Cluster
resource "aws_ecs_cluster" "app_cluster" {
  name = "app-cluster"
}

# IAM role for ECS task execution
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole"

  assume_role_policy = data.aws_iam_policy_document.ecs_task_assume_role_policy.json
}

data "aws_iam_policy_document" "ecs_task_assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

# ECS Task Definition running nginx
resource "aws_ecs_task_definition" "app" {
  family                   = "nginx-app-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([
    {
      name      = "nginx"
      image     = "nginx:latest"
      portMappings = [
        {
          containerPort = 80
          hostPort      = 80
          protocol      = "tcp"
        }
      ]
      essential = true
    }
  ])
}

# Security Group for ECS Service
resource "aws_security_group" "ecs_sg" {
  name        = "ecs-service-sg"
  description = "Allow inbound traffic to ecs service"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    description = "HTTP from anywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# ECS Service
resource "aws_ecs_service" "app_service" {
  name            = "nginx-app-service"
  cluster         = aws_ecs_cluster.app_cluster.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = data.aws_subnets.default.ids
    security_groups = [aws_security_group.ecs_sg.id]
    assign_public_ip = true
  }

  depends_on = [
    aws_iam_role_policy_attachment.ecs_task_execution_role_policy
  ]
}

# Output
output "ecs_service_name" {
  description = "Name of the deployed ECS service"
  value       = aws_ecs_service.app_service.name
}

output "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  value       = aws_ecs_cluster.app_cluster.name
}

output "security_group_id" {
  description = "Security group ID used by ECS service"
  value       = aws_security_group.ecs_sg.id
}
```

---

### Instructions

1. Create the S3 bucket `terraform-scripts-deployment-664091862099` in `eu-west-2` for storing your state file.
2. Make sure the IAM role `terraform_deploy_role` exists in account `664091862099` and your credentials have permission to assume it.
3. From your local machine or CI/CD environment with Terraform installed:
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```
4. This will create an ECS Fargate service running an Nginx container in the default VPC/subnets in `eu-west-2`.

---

### Customize for your application

- Replace the ECS task definition container details with your app container image, environment variables, and resources.
- Use your own VPC and subnet IDs if needed instead of default.
- Add other resources your app requires (ALB, RDS, etc).

---

If you want me to create a script with different AWS resources or more details about your real app, just let me know!