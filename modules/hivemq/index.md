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
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>hivemq</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/hivemq/
    maintainer: core
    example: |
      ```javascript
      const container = await new HiveMQContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/hivemq --save-dev
      ```
description: |
  HiveMQ is an MQTT broker and a client based messaging platform designed for the fast, efficient and reliable movement of data to and from connected IoT devices.
---