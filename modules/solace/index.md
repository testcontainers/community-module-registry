---
title: Solace PubSub+
categories:
  - message-broker
docs:
  - id: java
    url: https://java.testcontainers.org/modules/solace/
    maintainer: core
    example: |
      ```java
      var solaceContainer = new SolaceContainer(DockerImageName.parse("solace/solace-pubsub-standard:10.2"));
      solace.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-solace</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/solace/
    maintainer: core
    example: |
      ```go
      solaceContainer, err := solace.Run(context.Background(), "solace/solace-pubsub-standard:latest")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/solace
      ```
description: |
  Solace PubSub+ is an event streaming, management and monitoring platform that gives you everything you need to design, deploy and manage an event-driven system. Stream events across hybrid, multi-cloud and IoT environments, quickly, reliably and securely. Manage your entire events ecosystem.
---
