---
title: Weaviate
categories:
  - vector-database
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
description: |
  Weaviate is an open source, AI-native vector database that helps developers create intuitive and reliable AI-powered applications.
---