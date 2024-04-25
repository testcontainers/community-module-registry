---
title: Distribution Registry
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/registry/
    maintainer: core
    example: |
      ```go
      registryContainer, err := registry.RunContainer(context.Background(), testcontainers.WithImage("registry:2.8.3"))
      ```
description: |
  The Open Source Registry implementation for storing and distributing container images and other content using the OCI Distribution Specification.
---
