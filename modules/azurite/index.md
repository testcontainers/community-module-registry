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
description: |
  A lightweight server clone of Azure Storage.
---