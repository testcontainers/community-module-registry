---
title: Weaviate
categories:
  - vector-database
officialPartner:
  name: Weaviate
  url: https://weaviate.io/
docs:
  - id: java
    url: https://java.testcontainers.org/modules/weaviate/
    maintainer: core
    example: |
      ```java
      var weaviate = new WeaviateContainer("semitechnologies/weaviate:1.23.9");
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/weaviate/
    maintainer: core
    example: |
      ```go
      weaviateContainer, err := weaviate.RunContainer(ctx, testcontainers.WithImage("semitechnologies/weaviate:1.23.9"))
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/weaviate/
    maintainer: core
    example: |
      ```javascript
      const container = await new WeaviateContainer().start();
      ```
description: |
  Weaviate is an open source, AI-native vector database that helps developers create intuitive and reliable AI-powered applications.
---