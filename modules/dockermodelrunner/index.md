---
title: Docker Model Runner
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/dockermodelrunner/
    maintainer: core
    example: |
      ```go
      dmrContainer, err := dockermodelrunner.Run(context.Background())
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/dockermodelrunner
      ```
description: |
    Docker Model Runner is a faster, simpler way to run and test AI models locally, right from your existing workflow.
---
