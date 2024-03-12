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
      var neo4j = new Neo4jContainer<>(DockerImageName.parse("neo4j:4.4"));
      neo4j.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/neo4j/
    maintainer: core
    example: |
      ```go
      neo4jContainer, err := neo4j.RunContainer(ctx,
        testcontainers.WithImage("neo4j:4.4"),
        neo4j.WithAdminPassword("letmein!"),
        neo4j.WithLabsPlugin(neo4j.Apoc),
      )
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
  - id: nodejs
    url: https://node.testcontainers.org/modules/neo4j/
    maintainer: core
    example: |
      ```javascript
      const container = await new Neo4jContainer().start();
      ```
description: |
  Neo4j is a highly scalable open source graph database management system.
---