---
title: NATS
categories:
  - message-broker
docs:
  - id: java
    url: https://github.com/AmadeusITGroup/nats-testcontainers-java
    maintainer: community
    example: |
      ```java
      var nats = new NatsContainer("nats:2.9");
      nats.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.github.amadeusitgroup.testcontainers</groupId>
          <artifactId>nats</artifactId>
          <version>1.0.9</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/nats/
    maintainer: core
    example: |
      ```go
      natsContainer, err := nats.Run(context.Background(), "nats:2.9")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/nats
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Nats
    maintainer: core
    example: |
      ```csharp
      var natsContainer = new NatsBuilder()
        .WithImage("nats:2.9")
        .Build();
      await natsContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Nats
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/nats/
    maintainer: core
    example: |
      ```javascript
      const container = await new NatsContainer("nats:2.8.4-alpine").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/nats --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/nats/README.html
    maintainer: core
    example: |
      ```python
      with NatsContainer() as nats_container:
          client = await nats.connect(nats_container.nats_uri())
      ```
    installation: |
      ```bash
      pip install testcontainers[nats]
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/nats/struct.Nats.html
    maintainer: community
    example: |
      ```rust
      testcontainers_modules::nats::Nats::default().start()
      ```
    installation: |
      ```bash
      cargo add -F nats --dev testcontainers-modules
      ```
description: |
  NATS is an open-source messaging system that enables applications to securely communicate across any combination of cloud vendors, on-premise, edge, web and mobile, and devices.
---
