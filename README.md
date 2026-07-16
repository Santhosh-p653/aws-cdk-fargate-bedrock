# AWS CDK + ECS Fargate + Amazon Bedrock

A cloud-native application built with **AWS CDK (Python)** that deploys a containerized **Flask** web application on **Amazon ECS Fargate** and integrates with **Amazon Bedrock** for AI inference.

This project is being built as a learning resource to understand Infrastructure as Code (IaC), containerization, AWS deployment, and cloud engineering best practices.

---

## Features

- Infrastructure as Code using AWS CDK
- Python Flask backend
- HTML, CSS and JavaScript frontend
- Docker containerization
- Amazon ECS Fargate deployment
- Amazon Bedrock integration
- Infrastructure testing using Pytest
- CloudWatch logging
- Safe deployment with `cdk diff`
- Resource cleanup using `cdk destroy`

---

## Architecture

```text
Browser
    │
HTML / CSS / JavaScript
    │
Flask Backend
    │
Amazon Bedrock
    │
AI Response

Deployment

AWS CDK
    │
CloudFormation
    │
Amazon ECS Fargate
```

---

## Project Structure

```text
.
├── cloud_fargate_bedrock/      # AWS CDK Infrastructure
├── webapp/                     # Flask Application
│   ├── templates/
│   ├── static/
│   ├── services/
│   ├── app.py
│   └── requirements.txt
├── tests/                      # Infrastructure Tests
├── docs/
├── Dockerfile
├── app.py
├── cdk.json
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

---

## Technology Stack

- AWS CDK
- Amazon ECS
- AWS Fargate
- Amazon Bedrock
- CloudFormation
- Python
- Flask
- Docker
- Boto3
- Pytest

---

## Development Workflow

```bash
pytest

cdk synth

cdk diff

cdk deploy

cdk destroy
```

---

## Learning Goals

- Learn AWS CDK from first principles
- Understand Infrastructure as Code
- Deploy containerized applications on AWS
- Work with Amazon ECS and Fargate
- Integrate Amazon Bedrock
- Write infrastructure tests
- Follow production-style deployment workflows

---

## Current Progress

- [x] AWS CLI configured
- [x] AWS CDK installed
- [x] Project initialized
- [x] GitHub repository created
- [ ] Flask web application
- [ ] Docker container
- [ ] ECS Fargate deployment
- [ ] Amazon Bedrock integration
- [ ] Infrastructure tests
- [ ] CloudWatch logging

---

## Future Improvements

- GitHub Actions CI/CD
- Application Load Balancer
- HTTPS with ACM
- Amazon ECR
- Secrets Manager
- CloudWatch dashboards
- Auto Scaling
- Cost monitoring

---

## License

This project is licensed under the MIT License.