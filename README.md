# Serverless To-Do REST API

## Project Overview

This project demonstrates the architecture of a Serverless REST API built on AWS. It uses managed AWS services to provide a scalable, secure, and cost-effective solution for managing To-Do tasks.

---

## AWS Services Used

- Amazon S3
- Amazon CloudFront
- Amazon API Gateway
- AWS Lambda
- Amazon Cognito
- Amazon DynamoDB

---

## Architecture Diagram

![Architecture Diagram](architecture/architecture-diagram.png)

---

## Project Structure

```
serverless-todo-api/
│
├── architecture/
│   └── architecture-diagram.png
│
├── docs/
│
├── lambda/
│   └── handler.py
│
├── README.md
│
└── .gitignore
```

---

## Architecture Flow

1. User accesses the application.
2. CloudFront delivers the static website from Amazon S3.
3. API requests are sent to API Gateway.
4. Amazon Cognito authenticates users.
5. AWS Lambda processes the request.
6. DynamoDB stores and retrieves task data.

---

## Author

GitHub Project for AWS Serverless Architecture.