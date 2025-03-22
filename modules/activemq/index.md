---
title: ActiveMQ
categories:
  - message-broker
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.ActiveMq
    maintainer: core
    example: |
      ```csharp
      var activeMqContainer = new ArtemisBuilder()
        .WithImage("apache/activemq-artemis:2.31.2")
        .Build();
      await activeMqContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.ActiveMq
      ```
description: |
  Apache ActiveMQ® is the most popular open source, multi-protocol, Java-based message broker. It supports industry standard protocols so users get the benefits of client choices across a broad range of languages and platforms. Connect from clients written in JavaScript, C, C++, Python, .Net, and more. Integrate your multi-platform applications using the ubiquitous AMQP protocol. Exchange messages between your web applications using STOMP over websockets. Manage your IoT devices using MQTT. Support your existing JMS infrastructure and beyond. ActiveMQ offers the power and flexibility to support any messaging use-case.
---
