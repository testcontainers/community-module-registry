---
title: Azure Cosmos DB
categories:
  - cloud
docs:
  - id: java
    url: https://java.testcontainers.org/modules/azure/
    maintainer: core
    example: |
      ```java
      var cosmos = new CosmosDBEmulatorContainer(
        DockerImageName.parse("mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest")
      );
      cosmos.start();
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.CosmosDb
    maintainer: core
    example: |
      ```csharp
      var cosmosDbContainer = new CosmosDbBuilder()
        .WithImage("mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest")
        .Build();
      await cosmosDbContainer.StartAsync();
      ```
description: |
  Azure Cosmos DB is a fully managed, horizontally scalable, NoSQL and relational database.
---
