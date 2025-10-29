---
title: Pulsar
categories:
  - message-broker
officialPartner:
  name: StreamNative
  url: https://streamnative.io/
docs:
  - id: java
    url: https://java.testcontainers.org/modules/pulsar/
    maintainer: official
    example: |
      ```java
      var pulsar = new PulsarContainer(DockerImageName.parse("apachepulsar/pulsar:2.10.0"));
      pulsar.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-pulsar</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/pulsar/
    maintainer: official
    example: |
      ```go
      pulsarContainer, err := pulsar.Run(context.Background(),
        "apachepulsar/pulsar:2.10.0",
        pulsar.WithPulsarEnv("brokerDeduplicationEnabled", "true"),
        pulsar.WithFunctionsWorker(),
        pulsar.WithTransactions(),
      )
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/pulsar
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Pulsar
    maintainer: core
    example: |
      ```csharp
      var pulsarContainer = new PulsarBuilder()
        .WithImage("apachepulsar/pulsar:2.10.0")
        .Build();
      await pulsarContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Pulsar
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/pulsar/struct.Pulsar.html
    maintainer: community
    example: |
      ```rust
      testcontainers_modules::pulsar::Pulsar::default().start()
      ```
    installation: |
      ```bash
      cargo add -F pulsar --dev testcontainers-modules
      ```
description: |
  Apache Pulsar is an open-source, distributed messaging and streaming platform. Messages can be consumed and acknowledged individually or consumed as streams with less than 5ms of latency.
---
