---
title: Mosquitto
categories:
  - message-broker
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Mosquitto
    maintainer: core
    example: |
      ```csharp
      var mosquittoContainer = new MosquittoBuilder()
        .WithImage("eclipse-mosquitto:2.0")
        .Build();
      await mosquittoContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Mosquitto
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/mqtt/README.html
    maintainer: core
    example: |
      ```python
      with MosquittoContainer(image = "eclipse-mosquitto:2.0.20") as mosquitto_broker:
          mqtt_client = mosquitto_broker.get_client()
      ```
    installation: |
      ```bash
      pip install testcontainers[mqtt]
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/mosquitto/struct.Mosquitto.html
    maintainer: community
    example: |
      ```rust
      testcontainers_modules::mosquitto::Mosquitto::default().start()

      let broker_url = format!(
          "{}:{}",
          mosquitto_instance.get_host().unwrap(),
          mosquitto_instance.get_host_port_ipv4(1883).unwrap()
      );
      ```
    installation: |
      ```bash
      cargo add -F mosquitto --dev testcontainers-modules
      ```
description: |
  Eclipse Mosquitto is an open source message broker which implements MQTT version 5, 3.1.1 and 3.1.
---
