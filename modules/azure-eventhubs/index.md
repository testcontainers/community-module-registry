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

      AzureEventHubsContainer eventHubs = new AzureEventHubsContainer("mcr.microsoft.com/azure-messaging/eventhubs-emulator:2.0.1")
         .acceptLicense()
         .withNetwork(network)
         .withAzuriteContainer(azurite);
      eventHubs.start();
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
description: |
  Azure Event Hubs emulator is designed to offer a local development experience for Azure Event Hubs.
---
