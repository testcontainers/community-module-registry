---
title: ArangoDB
categories:
  - nosql-database
docs:
  - id: java
    url: https://github.com/GoodforGod/arangodb-testcontainers
    maintainer: community
    example: |
      ```java
      var arango = new ArangoContainer();
      arango.start();
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.ArangoDb
    maintainer: core
    example: |
      ```csharp
      var arangodb = new ArangoDbBuilder()
        .WithImage("arangodb:3.11.5")
        .Build();
      arangodb.StartAsync();
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/arangodb/
    maintainer: core
    example: |
      ```javascript
      const container = await new ArangoDBContainer().start();
      ```
description: |
  ArangoDB is a free and open-source native graph database system. It supports three data models; graphs, JSON documents, and key/value.
---