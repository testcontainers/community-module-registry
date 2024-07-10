---
title: Smocker
categories:
  - web
docs:
  - id: go
    url: https://github.com/jespino/testcontainers-go-smocker
    maintainer: community
    example: |
      ```go
      container, err := smocker.RunContainer(context.Background(), testcontainers.WithImage("thiht/smocker:0.18.5"));
      ```
    installation: |
      ```bash
      go get github.com/jespino/testcontainers-go-smocker
      ```
description: |
  Smocker is a simple and efficient HTTP mock server.
---
