---
title: Azure Event Hubs
categories:
  - cloud
docs:
  - id: java
    url: https://java.testcontainers.org/modules/azure/#azure-event-hubs-emulator
    maintainer: core
    example: |
      ```java
      Network network = Network.newNetwork();
      AzuriteContainer azurite = new AzuriteContainer("mcr.microsoft.com/azure-storage/azurite:3.33.0")
          .withNetwork(network);
      azurite.start();

      var eventHubs = new EventHubsEmulatorContainer("mcr.microsoft.com/azure-messaging/eventhubs-emulator:2.0.1")
         .acceptLicense()
         .withNetwork(network)
         .withAzuriteContainer(azurite);
      eventHubs.start();
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
    url: https://golang.testcontainers.org/modules/azure/#eventhubs
    maintainer: core
    example: |
      ```go
      eventhubsContainer, err := eventhubs.Run(context.Background(), "mcr.microsoft.com/azure-messaging/eventhubs-emulator:2.0.1")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/azure
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.EventHubs
    maintainer: core
    example: |
      ```csharp
      var eventHubsContainer = new EventHubsBuilder("mcr.microsoft.com/azure-messaging/eventhubs-emulator:latest")
        .Build();
      await eventHubsContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.EventHubs
      ```
description: |
  Azure Event Hubs emulator is designed to offer a local development experience for Azure Event Hubs.
---
