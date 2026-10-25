---
title: Socat
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/socat/
    maintainer: core
    example: |
      ```go
      socatContainer, err := socat.Run(
        context.Background(),
        socat.DefaultImage,
        socat.WithTarget(socat.NewTarget(8080, "service")),
      )
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/socat
      ```
description: |
  Socat provides a utility container for TCP port forwarding and network
  tunneling between services.
---
