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
description: |
  Qdrant is a vector database & vector similarity search engine. It deploys as an API service providing search for the nearest high-dimensional vectors.
---