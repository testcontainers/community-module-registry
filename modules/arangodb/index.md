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
    installation: |
      ```xml
      <dependency>
          <groupId>com.github.goodforgod</groupId>
          <artifactId>arangodb-testcontainers</artifactId>
          <version>3.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.ArangoDb
    maintainer: core
    example: |
      ```csharp
      var arangodb = new ArangoDbBuilder()
        .WithImage("arangodb:3.11.5")
        .Build();
      await arangodb.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.ArangoDb --version 3.9.0
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/arangodb/
    maintainer: core
    example: |
      ```javascript
      const container = await new ArangoDBContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/arangodb --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/arangodb/README.html
    maintainer: community
    example: |
      ```python
      with ArangoDbContainer("arangodb:3.11.8") as arango:
        client = ArangoClient(hosts=arango.get_connection_url())
        sys_db = client.db(username="root", password="passwd")
        sys_db.create_database("test")
      ```
    installation: |
      ```bash
      pip install testcontainers[arangodb]
      ```
description: |
  ArangoDB is a free and open-source native graph database system. It supports three data models; graphs, JSON documents, and key/value.
---
