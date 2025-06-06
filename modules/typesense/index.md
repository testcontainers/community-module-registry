---
title: Typesense
categories:
  - vector-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/typesense/
    maintainer: core
    example: |
      ```java
      var typesense = new TypesenseContainer(DockerImageName.parse("typesense/typesense:27.1"));
      typesense.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>typesense</artifactId>
          <version>1.20.3</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Typesense
    maintainer: core
    example: |
      ```csharp
      var typesenseContainer = new TypesenseBuilder()
        .WithImage("typesense/typesense:28.0")
        .Build();
      await typesenseContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Typesense
      ```
description: |
  Typesense is a modern, blazing-fast, developer-friendly, open source search engine.
---
