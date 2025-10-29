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
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-activemq</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/artemis/
    maintainer: core
    example: |
      ```go
      artemisContainer, err := artemis.Run(context.Background(), "docker.io/apache/activemq-artemis:2.30.0-alpine")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/artemis
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
    installation: |
      ```bash
      dotnet add package Testcontainers.ActiveMq
      ```
description: |
  Apache ActiveMQ Artemis is an open source project to build a multi-protocol, embeddable, very high performance, clustered, asynchronous messaging system.
---
