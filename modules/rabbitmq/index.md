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
  - id: go
    url: https://golang.testcontainers.org/modules/rabbitmq/
    maintainer: core
    example: |
      ```go
      rabbitmqContainer, err := rabbitmq.RunContainer(ctx, testcontainers.WithImage("rabbitmq:3.7.25-management-alpine"),
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
description: |
  RabbitMQ is an open-source message-broker software that originally implemented the Advanced Message Queuing Protocol and has since been extended with a plug-in architecture to support Streaming Text Oriented Messaging Protocol, MQ Telemetry Transport, and other protocols.
---