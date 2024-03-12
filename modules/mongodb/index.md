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
  - id: go
    url: https://golang.testcontainers.org/modules/mongodb/
    maintainer: core
    example: |
      ```go
      mongoDBContainer, err := mongodb.RunContainer(ctx, testcontainers.WithImage("mongo:6"))
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
  - id: nodejs
    url: https://node.testcontainers.org/modules/mongodb/
    maintainer: core
    example: |
      ```javascript
      const mongodbContainer = await new MongoDBContainer().start();
      ```
description: |
  MongoDB is a source-available cross-platform document-oriented database program.
---