---
title: Resend
categories:
  - other
docs:
  - id: go
    url: https://github.com/mdelapenya/testcontainers-go-resend
    maintainer: community
    example: |
      ```go
      ctr, err := resend.Run(ctx, resend.DefaultImage)
      ```
    installation: |
      ```bash
      go get github.com/mdelapenya/testcontainers-go-resend
      ```
  - id: nodejs
    url: https://github.com/mdelapenya/testcontainers-node-resend
    maintainer: community
    example: |
      ```javascript
      const container = await new ResendContainer().start();
      ```
    installation: |
      ```bash
      npm install --save-dev @mdelapenya/testcontainers-resend
      ```
description: |
  Resend is an email API built for developers. This module provides a mock Resend API for integration testing, using [Microcks](https://microcks.io/) under the hood to serve mock responses based on the official [Resend OpenAPI spec](https://github.com/resend/resend-openapi).
---
