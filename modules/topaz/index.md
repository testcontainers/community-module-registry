---
title: Topaz
categories:
  - cloud
docs:
  - id: dotnet
    url: https://github.com/TheCloudTheory/topaz-testcontainers
    maintainer: community
    example: |
      ```csharp
      const string defaultSubscriptionId = "00000000-0000-0000-0000-000000000001";
      new TopazBuilder()
            .WithDefaultSubscription(Guid.Parse(defaultSubscriptionId))
            .WithLoggingToFile()
            .WithLogLevel(TopazLogLevel.Debug)
            .WithName("topaz.local.dev")
            .Build();

      await Container.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package TheCloudTheory.Topaz.Testcontainers
      ```
description: |
  Topaz is a local Azure emulator that supports multiple Azure services including Storage, Service Bus, Event Hubs, Cosmos DB, Key Vault, App Service, and Container Registry. It also emulated Entra ID authentication flows.
---
