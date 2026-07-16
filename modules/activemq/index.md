---
title: ActiveMQ Classic
categories:
  - message-broker
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/activemq/
    maintainer: core
    example: |
      ```go
      activemqContainer, err := activemq.Run(context.Background(), "apache/activemq-classic:5.18.7")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/activemq
      ```
description: |
  Apache ActiveMQ Classic is an open source, multi-protocol, Java-based message broker.
---
