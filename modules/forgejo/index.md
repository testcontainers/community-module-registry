---
title: Forgejo
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/forgejo/
    maintainer: core
    example: |
      ```go
      forgejoContainer, err := forgejo.Run(ctx, "codeberg.org/forgejo/forgejo:11")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/forgejo
      ```
description: |
  Forgejo is a self-hosted, lightweight Git forge and a community-driven fork of Gitea, providing a code hosting solution.
---
