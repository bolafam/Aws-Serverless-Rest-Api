# Architecture Notes

## AWS Services

- Amazon S3 hosts the static website.
- Amazon CloudFront delivers content globally.
- AWS WAF protects the API from common web attacks.
- Amazon API Gateway exposes REST endpoints.
- Amazon Cognito authenticates users.
- AWS Lambda executes business logic.
- Amazon DynamoDB stores application data.
- AWS X-Ray provides distributed tracing and monitoring.
## AWS X-Ray

AWS X-Ray provides distributed tracing across API Gateway, AWS Lambda, and Amazon DynamoDB. It helps monitor request flow, identify latency, and troubleshoot performance issues in the serverless architecture.
## Amazon Cognito

Amazon Cognito handles user authentication using User Pools and JWT tokens. API Gateway validates JWT tokens before invoking AWS Lambda functions.

## AWS WAF

AWS WAF protects the REST API using managed rule groups, rate limiting, and web attack protection such as SQL injection and XSS filtering.

## Amazon DynamoDB

The application stores customer records in a DynamoDB table using the `id` attribute as the partition key. Additional attributes include `name` and `email`.

## Amazon CloudFront

CloudFront delivers static website content from Amazon S3 and forwards API requests securely to AWS WAF and API Gateway.

## Amazon S3

Amazon S3 hosts the static frontend files that are delivered globally through CloudFront.
