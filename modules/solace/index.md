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
description: |
  Solace PubSub+ is an event streaming, management and monitoring platform that gives you everything you need to design, deploy and manage an event-driven system. Stream events across hybrid, multi-cloud and IoT environments, quickly, reliably and securely. Manage your entire events ecosystem.
---