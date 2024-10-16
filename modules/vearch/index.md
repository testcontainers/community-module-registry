---
title: Vearch
categories:
  - vector-database
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/vearch/
    maintainer: core
    example: |
      ```go
      vearchContainer, err := vearch.Run(ctx, "vearch/vearch:3.5.1")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/vearch
      ```
description: |
  Vearch is a cloud-native distributed vector database for efficient similarity search of embedding vectors in your AI applications.
---
