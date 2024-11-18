---
title: TigerBeetle
categories:
  - relational-database
docs:
  - id: go
    url: https://github.com/mkadirtan/testcontainers-tigerbeetle-go
    maintainer: community
    installation: |
      ```bash
      go get -u github.com/mkadirtan/testcontainers-tigerbeetle-go@latest
      ```
    example: |
      ```go
      tbContainer, err := tigerbeetle.Run(ctx, "https://ghcr.io/tigerbeetle/tigerbeetle:latest")
      ```
description: |
  TigerBeetle is a distributed financial accounting database designed for mission critical safety and performance.
---
