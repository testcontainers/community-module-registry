---
title: Grafana
categories:
  - other
docs:
  - id: java
    url: https://java.testcontainers.org/modules/grafana/
    maintainer: core
    example: |
      ```java
      var lgtm = new LgtmStackContainer("grafana/otel-lgtm:0.6.0");
      lgtm.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-grafana</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/grafana-lgtm/
    maintainer: core
    example: |
      ```go
      grafanaLgtmContainer, err := grafanalgtm.Run(context.Background(), "grafana/otel-lgtm:0.6.0")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/grafanalgtm
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Grafana
    maintainer: core
    example: |
      ```csharp
      var grafanaContainer = new GrafanaBuilder("grafana/grafana:12.2")
        .Build();
      await grafanaContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Grafana
      ```
description: |
  Grafana is the open source analytics & monitoring solution for every database.
---
