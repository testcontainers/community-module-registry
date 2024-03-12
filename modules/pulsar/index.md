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
  - id: go
    url: https://golang.testcontainers.org/modules/pulsar/
    maintainer: official
    example: |
      ```go
      pulsarContainer, err := pulsar.RunContainer(ctx,
        testcontainers.WithImage("apachepulsar/pulsar:2.10.0"),
        pulsar.WithPulsarEnv("brokerDeduplicationEnabled", "true"),
        pulsar.WithFunctionsWorker(),
        pulsar.WithTransactions(),
      )
      ```
description: |
  Apache Pulsar is an open-source, distributed messaging and streaming platform. Messages can be consumed and acknowledged individually or consumed as streams with less than 5ms of latency.
---