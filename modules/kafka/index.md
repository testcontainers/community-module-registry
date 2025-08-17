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
      var kafka = new KafkaContainer("apache/kafka-native:3.8.0");
      kafka.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>kafka</artifactId>
          <version>1.20.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/kafka/
    maintainer: core
    example: |
      ```go
      kafkaContainer, err := kafka.Run(context.Background(), "confluentinc/confluent-local:7.5.0")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/kafka
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
    installation: |
      ```bash
      dotnet add package Testcontainers.Kafka
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/kafka/
    maintainer: core
    example: |
      ```javascript
      const kafkaContainer = await new KafkaContainer("confluentinc/cp-kafka:7.2.2").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/kafka --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/kafka/README.html
    maintainer: core
    example: |
      ```python
      with KafkaContainer() as kafka:
          connection = kafka.get_bootstrap_server()
      ```
    installation: |
      ```bash
      pip install testcontainers[kafka]
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/kafka/index.html
    maintainer: community
    example: |
      ```rust
      testcontainers_modules::kafka::confluent::Kafka::default().start()
      // or also: testcontainers_modules::kafka::apache::Kafka::default().start()
      ```
    installation: |
      ```bash
      cargo add -F kafka --dev testcontainers-modules
      ```
description: |
  Kafka is an open-source distributed event streaming platform for high-performance data pipelines, streaming analytics, data integration, and mission-critical applications.
---
