---
title: HomeCloud
categories:
  - cloud
docs:
  - id: go
    url: https://github.com/solinode/homecloud/tree/main/integrations/testcontainers-go
    maintainer: official
    example: |
      ```go
      hc, err := homecloud.Run(context.Background(), homecloud.DefaultImage)
      cfg := hc.AWSConfig()
      ```
    installation: |
      ```bash
      go get github.com/solinode/homecloud/integrations/testcontainers-go
      ```
  - id: python
    url: https://github.com/solinode/homecloud/tree/main/integrations/testcontainers-python
    maintainer: official
    example: |
      ```python
      with HomeCloudContainer() as hc:
          s3 = hc.get_client("s3")
          s3.create_bucket(Bucket="test")
      ```
    installation: |
      ```bash
      pip install "testcontainers-homecloud @ git+https://github.com/solinode/homecloud#subdirectory=integrations/testcontainers-python"
      ```
description: |
  HomeCloud is a self-hosted, AWS-compatible cloud. The AWS CLI, SDKs and Terraform work against it, and services such as S3, Lambda, RDS, DynamoDB and SQS run as real containers. AGPL-3.0 licensed.
---
