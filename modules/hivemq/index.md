---
title: HiveMQ
categories:
  - message-broker
docs:
  - id: java
    url: https://java.testcontainers.org/modules/hivemq/
    maintainer: core
    example: |
      ```java
      var hivemqCe = new HiveMQContainer(DockerImageName.parse("hivemq/hivemq-ce")
        .withTag("2021.3"))
      hivemqCe.start();
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/hivemq/
    maintainer: core
    example: |
      ```javascript
      const container = await new HiveMQContainer().start();
      ```
description: |
  HiveMQ is an MQTT broker and a client based messaging platform designed for the fast, efficient and reliable movement of data to and from connected IoT devices.
---