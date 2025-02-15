---
title: Azurite
categories:
  - cloud
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/azurite/
    maintainer: core
    example: |
      ```go
      azuriteContainer, err := azurite.Run(ctx, "mcr.microsoft.com/azure-storage/azurite:3.28.0")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/azurite
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
description: |
  A lightweight server clone of Azure Storage.
---
