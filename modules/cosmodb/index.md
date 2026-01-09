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
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-azure</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/azure/#cosmosdb
    maintainer: core
    example: |
      ```go
      cosmosContainer, err := cosmosdb.Run(context.Background(), "mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/azure
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.CosmosDb
    maintainer: core
    example: |
      ```csharp
      var cosmosDbContainer = new CosmosDbBuilder("mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest")
        .Build();
      await cosmosDbContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.CosmosDb
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/cosmosdb/
    maintainer: core
    example: |
      ```javascript
      const container = await new AzureCosmosDbEmulatorContainer(
        "mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:vnext-EN20250228"
      ).start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/azure-cosmosdb-emulator --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/cosmosdb/README.html
    maintainer: core
    example: |
      ```python
      with CosmosDBNoSQLEndpointContainer() as emulator:
          client = CosmosClient(url=emulator.url, credential=emulator.key, connection_verify=False)
          db = client.create_database_if_not_exists("test")
      ```
    installation: |
      ```bash
      pip install testcontainers[cosmosdb]
      ```
description: |
  Azure Cosmos DB is a fully managed, horizontally scalable, NoSQL and relational database.
---
