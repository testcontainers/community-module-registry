---
title: Docker Sandboxes (sbx)
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/sbx/
    maintainer: core
    example: |
      ```go
      import _ "github.com/testcontainers/testcontainers-go/modules/sbx"
      ```

      ```bash
      TESTCONTAINERS_PROVIDER=sbx go test ./...
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/sbx
      ```
description: |
  Docker Sandboxes support runs Testcontainers for Go inside a provider-owned
  Docker Sandbox for the test process.
---
