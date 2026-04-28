---
title: MiniStack
categories:
  - cloud
docs:
  - id: java
    url: https://github.com/ministackorg/testcontainers-ministack
    maintainer: official
    example: |
      ```java
      var ministack = new MiniStackContainer("latest");
      ministack.start();
      String endpoint = ministack.getEndpoint();
      ```
description: |
  MiniStack is a free, open-source local AWS emulator. It runs 40+ AWS services on a single port (4566) — S3, SQS, SNS, DynamoDB, Lambda, IAM, CloudFormation, and more. Drop-in compatible with boto3, AWS CLI, Terraform, CDK, and any AWS SDK. MIT licensed.
---
