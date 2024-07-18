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
      var weaviate = new WeaviateContainer("semitechnologies/weaviate:1.25.5");
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>weaviate</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/weaviate/
    maintainer: core
    example: |
      ```go
      weaviateContainer, err := weaviate.Run(ctx, "semitechnologies/weaviate:1.25.5")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/weaviate
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/weaviate/
    maintainer: core
    example: |
      ```javascript
      const container = await new WeaviateContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/weaviate --save-dev
      ```
description: |
  Weaviate is an open source, AI-native vector database that helps developers create intuitive and reliable AI-powered applications.
---
