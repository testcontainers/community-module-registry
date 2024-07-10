---
title: NATS
categories:
  - message-broker
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/nats/
    maintainer: core
    example: |
      ```go
      natsContainer, err := nats.Run(ctx, "nats:2.9")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/nats
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/nats/
    maintainer: core
    example: |
      ```javascript
      const container = await new NatsContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/nats --save-dev
      ```
description: |
  NATS is an open-source messaging system that enables applications to securely communicate across any combination of cloud vendors, on-premise, edge, web and mobile, and devices.
---