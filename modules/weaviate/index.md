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
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Weaviate
    maintainer: core
    example: |
      ```csharp
      var weaviateContainer = new WeaviateBuilder()
        .WithImage("semitechnologies/weaviate:1.26.14")
        .Build();
      await weaviateContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Weaviate
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
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/weaviate/README.html
    maintainer: core
    example: |
      ```python
      with WeaviateContainer() as container:
          with container.get_client() as client:
              client.is_live()
      ```
    installation: |
      ```bash
      pip install testcontainers[weaviate]
      ```
description: |
  Weaviate is an open source, AI-native vector database that helps developers create intuitive and reliable AI-powered applications.
---
