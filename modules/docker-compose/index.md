---
title: Docker Compose
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/features/docker_compose/
    maintainer: core
    example: |
      ```go
      stack, err := compose.NewDockerComposeWith(
        compose.WithStackFiles("docker-compose.yml"),
      )
      if err != nil {
        return err
      }
      defer stack.Down(context.Background())

      err = stack.Up(context.Background())
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/compose
      ```
description: |
  Docker Compose support lets Testcontainers for Go run a stack defined by a
  Compose file directly through the Compose v2 API.
---
