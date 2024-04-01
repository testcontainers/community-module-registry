---
title: Qdrant
categories:
  - vector-database
officialPartner:
  name: Qdrant
  url: https://qdrant.tech
docs:
  - id: java
    url: https://java.testcontainers.org/modules/qdrant/
    maintainer: official
    example: |
      ```java
      var qdrant = new QdrantContainer("qdrant/qdrant:v1.7.4");
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/qdrant/
    maintainer: official
    example: |
      ```go
      qdrantContainer, err := qdrant.RunContainer(ctx, testcontainers.WithImage("qdrant/qdrant:v1.7.4"))
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/qdrant/
    maintainer: core
    example: |
      ```javascript
      const container = await new QdrantContainer().start();
      ```
description: |
  Qdrant is the leading, high-performance, scalable, open-source vector database and search engine, essential for building the next generation of AI/ML applications. Qdrant is able to handle billions of vectors, supports the matching of semantically complex objects, and is implemented in Rust for performance, memory safety, and scale. Read more on www.qdrant.tech
---