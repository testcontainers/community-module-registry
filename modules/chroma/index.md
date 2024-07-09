---
title: Chroma
categories:
  - vector-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/chromadb/
    maintainer: core
    example: |
      ```java
      var chromadb = new ChromaDBContainer("chromadb/chroma:0.4.22");
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/chroma/
    maintainer: core
    example: |
      ```go
      chromaContainer, err := chroma.Run(ctx, "chromadb/chroma:0.4.22")
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/chromadb/
    maintainer: core
    example: |
      ```javascript
      const container = await new ChromaDBContainer().start();
      ```
description: |
  Chroma is the AI-native open-source embedding database.
---