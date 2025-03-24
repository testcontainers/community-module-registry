---
title: NATS
categories:
  - message-broker
docs:
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
description: |
  NATS is an open-source messaging system that enables applications to securely communicate across any combination of cloud vendors, on-premise, edge, web and mobile, and devices.
---
