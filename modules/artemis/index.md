---
title: Artemis
categories:
  - message-broker
docs:
  - id: java
    url: https://java.testcontainers.org/modules/activemq/
    maintainer: core
    example: |
      ```java
      var artemis = new ArtemisContainer("apache/activemq-artemis:2.30.0-alpine");
      artemis.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/artemis/
    maintainer: core
    example: |
      ```go
      artemisContainer, err := artemis.RunContainer(ctx, testcontainers.WithImage("docker.io/apache/activemq-artemis:2.30.0-alpine"))
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.ActiveMQ
    maintainer: core
    example: |
      ```csharp
      var artemisContainer = new ArtemisBuilder()
        .WithImage("apache/activemq-artemis:2.31.2")
        .Build();
        await artemisContainer.StartAsync();
      ```
description: |
  Apache ActiveMQ Artemis is an open source project to build a multi-protocol, embeddable, very high performance, clustered, asynchronous messaging system.
---