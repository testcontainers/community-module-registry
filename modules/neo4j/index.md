---
title: Neo4j
categories:
  - nosql-database
  - vector-database
officialPartner:
  name: neo4j
  url: https://neo4j.com
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/neo4j/
    maintainer: official
    example: |
      ```java
      var neo4j = new Neo4jContainer("neo4j:4.4");
      neo4j.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-neo4j</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/neo4j/
    maintainer: core
    example: |
      ```go
      neo4jContainer, err := neo4j.Run(context.Background(),
        "neo4j:4.4",
        neo4j.WithAdminPassword("letmein!"),
        neo4j.WithLabsPlugin(neo4j.Apoc),
      )
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/neo4j
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Neo4j
    maintainer: core
    example: |
      ```csharp
      var neo4jContainer = new Neo4jBuilder()
        .WithImage("neo4j:5.4")
        .Build();
      await neo4jContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Neo4j
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/neo4j/
    maintainer: core
    example: |
      ```javascript
      const container = await new Neo4jContainer("neo4j:4.4.12").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/neo4j --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/neo4j/README.html
    maintainer: core
    example: |
      ```python
      with Neo4jContainer() as neo4j, neo4j.get_driver() as driver, driver.session() as session:
          result = session.run("MATCH (n) RETURN n LIMIT 1")
          record = result.single()
      ```
    installation: |
      ```bash
      pip install testcontainers[neo4j]
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/oracle/free/struct.Oracle.html
    maintainer: community
    example: |
      ```rust
      // On slower machines more time needed than 60 seconds may be required (see `with_startup_timeout`).
      testcontainers_modules::oracle::free::Oracle::default().start()
      ```
    installation: |
      ```bash
      cargo add -F oracle --dev testcontainers-modules
      ```
description: |
  Neo4j is a highly scalable open source graph database management system.
---
