---
title: Docker in Docker (DinD)
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/dind/
    maintainer: core
    example: |
      ```go
      dindContainer, err := dind.Run(context.Background(), "docker:28.0.1-dind")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/dind
      ```
description: |
    Docker in Docker (DinD) is a Docker container that runs a Docker daemon.
---
