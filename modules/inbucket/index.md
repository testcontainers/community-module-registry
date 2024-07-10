---
title: Inbucket
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/inbucket/
    maintainer: core
    example: |
      ```go
      inbucketContainer, err := inbucket.Run(ctx, "inbucket/inbucket:sha-2d409bb")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/inbucket
      ```
description: |
  Inbucket is an email testing application; it will accept messages for any email address and make them available to view via a web interface.
---