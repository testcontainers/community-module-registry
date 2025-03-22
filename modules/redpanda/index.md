---
title: Redpanda
categories:
  - message-broker
officialPartner:
  name: Redpanda
  url: https://redpanda.com
docs:
  - id: java
    url: https://java.testcontainers.org/modules/redpanda/
    maintainer: official
    example: |
      ```java
      var redpanda = new RedpandaContainer(DockerImageName.parse("docker.redpanda.com/redpandadata/redpanda:v22.2.1"));
      redpanda.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>redpanda</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/redpanda/
    maintainer: core
    example: |
      ```go
      redpandaContainer, err := redpanda.Run(ctx, "docker.redpanda.com/redpandadata/redpanda:v23.1.7")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/redpanda
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Redpanda
    maintainer: core
    example: |
      ```csharp
      var redpandaContainer = new RedpandaBuilder()
        .WithImage("docker.redpanda.com/redpandadata/redpanda:v22.2.1")
        .Build();
      await redpandaContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Redpanda
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/redpanda/
    maintainer: core
    example: |
      ```javascript
      const redpandaContainer = await new RedpandaContainer("docker.redpanda.com/redpandadata/redpanda:v23.3.10").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/redpanda --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/kafka/README.html
    maintainer: core
    example: |
      ```python
      with RedpandaContainer() as redpanda:
        connection = redpanda.get_bootstrap_server()
      ```
    installation: |
      ```bash
      pip install testcontainers[kafka]
      ```
description: |
  Redpanda is the Kafka-compatible streaming data platform.
---
