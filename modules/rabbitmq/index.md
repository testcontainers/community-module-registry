---
title: RabbitMQ
categories:
  - message-broker
docs:
  - id: java
    url: https://java.testcontainers.org/modules/rabbitmq/
    maintainer: core
    example: |
      ```java
      var rabbit = new RabbitMQContainer(DockerImageName.parse("rabbitmq:3.7.25-management-alpine"));
      rabbit.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>rabbitmq</artifactId>
          <version>1.19.8</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/rabbitmq/
    maintainer: core
    example: |
      ```go
      rabbitmqContainer, err := rabbitmq.Run(ctx, "rabbitmq:3.7.25-management-alpine")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/rabbitmq
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.RabbitMq
    maintainer: core
    example: |
      ```csharp
      var rabbitMqContainer = new RabbitMqBuilder()
        .WithImage("rabbitmq:3.11")
        .Build();
      await rabbitMqContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.RabbitMq --version 3.9.0
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/rabbitmq/
    maintainer: core
    example: |
      ```javascript
      const container = await new RabbitMQContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/rabbitmq --save-dev
      ```
description: |
  RabbitMQ is an open-source message-broker software that originally implemented the Advanced Message Queuing Protocol and has since been extended with a plug-in architecture to support Streaming Text Oriented Messaging Protocol, MQ Telemetry Transport, and other protocols.
---