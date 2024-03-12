---
title: Kafka
categories:
  - message-broker
docs:
  - id: java
    url: https://java.testcontainers.org/modules/kafka/
    maintainer: core
    example: |
      ```java
      var kafka = new KafkaContainer(DockerImageName.parse("confluentinc/cp-kafka:6.2.1"));
      kafka.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/kafka/
    maintainer: core
    example: |
      ```go
      kafkaContainer, err := kafka.RunContainer(ctx, testcontainers.WithImage("confluentinc/confluent-local:7.5.0"))
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Kafka
    maintainer: core
    example: |
      ```csharp
      var kafkaContainer = new KafkaBuilder()
        .WithImage("confluentinc/cp-kafka:6.2.10")
        .Build();
      await kafkaContainer.StartAsync();
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/kafka/
    maintainer: core
    example: |
      ```javascript
      const kafkaContainer = await new KafkaContainer().withExposedPorts(9093).start();
      ```
description: |
  Kafka is an open-source distributed event streaming platform for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.
---