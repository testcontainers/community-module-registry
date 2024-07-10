---
title: Flyway
categories:
  - relational-database
docs:
  - id: go
    url: https://github.com/CyberOwlTeam/testcontainers-go-flyway
    maintainer: community
    example: |
      ```go
        flywayContainer, err := flyway.RunContainer(ctx, testcontainers.WithImage("flyway/flyway:10.15.0"))
      ```
    installation: |
      ```bash
      go get github.com/CyberOwlTeam/testcontainers-go-flyway
      ```
description: |
  Flyway by Redgate • Database Migrations Made Easy.
---
