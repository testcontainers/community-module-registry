---
title: MongoDB
categories:
  - nosql-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/mongodb/
    maintainer: core
    example: |
      ```java
      var mongoDBContainer = new MongoDBContainer(DockerImageName.parse("mongo:4.0.10"));
      mongoDBContainer.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>mongodb</artifactId>
          <version>1.19.8</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/mongodb/
    maintainer: core
    example: |
      ```go
      mongoDBContainer, err := mongodb.Run(ctx, "mongo:6")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/mongodb
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.MongoDb
    maintainer: core
    example: |
      ```csharp
      var mongoDbContainer = new MongoDbBuilder()
        .WithImage("mongo:6.0")
        .Build();
      await mongoDbContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.MongoDb --version 3.9.0
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/mongodb/
    maintainer: core
    example: |
      ```javascript
      const mongodbContainer = await new MongoDBContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/mongodb --save-dev
      ```
description: |
  MongoDB is a source-available cross-platform document-oriented database program.
---