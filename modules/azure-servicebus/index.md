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
      var servicebus = new AzureServiceBusContainer("mcr.microsoft.com/azure-messaging/servicebus-emulator:1.0.1")
          .acceptLicense()
          .withConfig(MountableFile.forClasspathResource("/service-bus-config.json"))
          .withNetwork(network)
          .withMsSqlServerContainer(mssqlServerContainer);
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
description: |
  The Azure Service Bus emulator offers a local development experience for the Service bus service.
---
