---
title: Garage
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/garage/
    maintainer: core
    example: |
      ```go
      garageContainer, err := garage.Run(context.Background(), "dxflrs/garage:v2.4.1")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/garage
      ```
description: |
  Garage is an open-source, S3-compatible object store designed for self-hosting.
  The Go module starts a single-node server with an initial access key and bucket for integration tests.
---
