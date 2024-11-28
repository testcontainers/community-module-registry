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
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>qdrant</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/qdrant/
    maintainer: official
    example: |
      ```go
      qdrantContainer, err := qdrant.Run(ctx, "qdrant/qdrant:v1.7.4")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/qdrant
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/qdrant/
    maintainer: core
    example: |
      ```javascript
      const container = await new QdrantContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/qdrant --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/qdrant/README.html
    maintainer: community
    example: |
      ```python
      with QdrantContainer() as qdrant:
        client = qdrant.get_client()
        client.get_collections()
      ```
    installation: |
      ```bash
      pip install testcontainers[qdrant]
      ```
description: |
  Qdrant is the leading, high-performance, scalable, open-source vector database and search engine, essential for building the next generation of AI/ML applications. Qdrant is able to handle billions of vectors, supports the matching of semantically complex objects, and is implemented in Rust for performance, memory safety, and scale. Read more on www.qdrant.tech
---
