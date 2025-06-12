---
title: Azurite
categories:
  - cloud
docs:
  - id: java
    url: https://java.testcontainers.org/modules/azure/#azurite-storage-emulator
    maintainer: core
    example: |
      ```java
      var container = new AzuriteContainer(DockerImageName.parse("mcr.microsoft.com/azure-storage/azurite:3.33.0"));
      container.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>azure</artifactId>
          <version>1.20.5</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/azure/#azurite
    maintainer: core
    example: |
      ```go
      azuriteContainer, err := azurite.Run(context.Background(), "mcr.microsoft.com/azure-storage/azurite:3.28.0")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/azure
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Azurite
    maintainer: core
    example: |
      ```csharp
      var AzuriteContainer = new AzuriteBuilder()
        .WithImage("mcr.microsoft.com/azure-storage/azurite:3.23.0")
        .Build();
      await AzuriteContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Azurite
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/azurite/README.html
    maintainer: core
    example: |
      ```python
      with AzuriteContainer() as azurite_container:
          connection_string = azurite_container.get_connection_string()
          client = BlobServiceClient.from_connection_string(
            connection_string,
            api_version="2019-12-12"
          )
      ```
    installation: |
      ```bash
      pip install testcontainers[azurite]
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/azurite/
    maintainer: core
    example: |
      ```javascript
      const container = await new AzuriteContainer("mcr.microsoft.com/azure-storage/azurite:3.33.0").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/azurite --save-dev
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/index.html
    maintainer: community
    example: |
      ```rust
      testcontainers_modules::azurite::Azurite::default().start()
      ```
    installation: |
      ```bash
      cargo add -F azurite --dev testcontainers-modules
      ```
description: |
  A lightweight server clone of Azure Storage.
---
