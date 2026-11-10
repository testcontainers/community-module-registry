---
title: understudy
categories:
  - cloud
docs:
  - id: go
    url: https://github.com/sustinbebustin/understudy/tree/main/testcontainers/go
    maintainer: official
    example: |
      ```go
      ctr, err := understudy.Run(ctx, understudy.DefaultImage)
      ```
    installation: |
      ```bash
      go get github.com/sustinbebustin/understudy/testcontainers/go
      ```
  - id: python
    url: https://github.com/sustinbebustin/understudy/tree/main/testcontainers/python
    maintainer: official
    example: |
      ```python
      import os
      from unittest.mock import patch

      import boto3
      from testcontainers_understudy import UnderstudyContainer

      with UnderstudyContainer() as understudy, patch.dict(os.environ, understudy.get_env()):
          sqs = boto3.client("sqs")
      ```
    installation: |
      ```bash
      pip install testcontainers-understudy
      ```
  - id: nodejs
    url: https://github.com/sustinbebustin/understudy/tree/main/testcontainers/node
    maintainer: official
    example: |
      ```javascript
      const understudy = await new UnderstudyContainer(UNDERSTUDY_IMAGE).start();
      ```
    installation: |
      ```bash
      npm install testcontainers-understudy --save-dev
      ```
description: |
  understudy is a local AWS emulator for testing event-driven systems: one binary that stands in for SQS, SNS, S3, DynamoDB, Lambda, EventBridge, Step Functions and eleven other services through `AWS_ENDPOINT_URL`.

  Timers run on one controllable clock, every call and delivery is recorded in a causal journal, and Lambda functions run in AWS's base images. The modules return the environment that points an AWS SDK at the container.

  Lambda functions and DynamoDB Local need the Docker socket: `WithDockerSocket()` in Go, `with_docker_socket()` in Python, `withDockerSocket()` in Node. Access to the socket is root-equivalent on the Docker host. See [Lambda and DynamoDB](https://github.com/sustinbebustin/understudy/blob/main/docs/guide/testcontainers-modules.md#lambda-and-dynamodb).

  Read more on [GitHub](https://github.com/sustinbebustin/understudy).
---
