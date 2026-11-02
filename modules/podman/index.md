---
title: Podman
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/podman/
    maintainer: core
    example: |
      ```go
      import _ "github.com/testcontainers/testcontainers-go/modules/podman"
      ```

      ```bash
      TESTCONTAINERS_PROVIDER=podman go test ./...
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/podman
      ```
description: |
  Podman support registers Podman as a Testcontainers for Go runtime provider
  using Podman's Docker-compatible API.
---
