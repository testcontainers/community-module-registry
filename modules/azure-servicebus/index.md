---
title: Azure Service Bus
categories:
  - cloud
docs:
  - id: java
    url: https://java.testcontainers.org/modules/azure/#azure-service-bus-emulator
    maintainer: core
    example: |
      ```java
      Network network = Network.newNetwork();

      MSSQLServerContainer<?> mssql = new MSSQLServerContainer<>("mcr.microsoft.com/mssql/server:2022-CU14-ubuntu-22.04")
          .acceptLicense()
          .withNetwork(network);
      mssql.start();

      var servicebus = new ServiceBusEmulatorContainer("mcr.microsoft.com/azure-messaging/servicebus-emulator:1.0.1")
          .acceptLicense()
          .withConfig(MountableFile.forClasspathResource("/service-bus-config.json"))
          .withNetwork(network)
          .withMsSqlServerContainer(mssql);
      servicebus.start();
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
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.ServiceBus
    maintainer: core
    example: |
      ```csharp
      var serviceBusContainer = new ServiceBusBuilder()
        .WithImage("mcr.microsoft.com/azure-messaging/servicebus-emulator:latest")
        .Build();
      await serviceBusContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.ServiceBus
      ```
description: |
  The Azure Service Bus emulator offers a local development experience for the Service bus service.
---
