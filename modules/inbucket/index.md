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
      inbucketContainer, err := inbucket.RunContainer(ctx, testcontainers.WithImage("inbucket/inbucket:sha-2d409bb"))
      ```
description: |
  Inbucket is an email testing application; it will accept messages for any email address and make them available to view via a web interface.
---