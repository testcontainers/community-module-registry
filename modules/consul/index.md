---
title: Consul
categories:
  - other
docs:
  - id: java
    url: https://java.testcontainers.org/modules/consul/
    maintainer: core
    example: |
      ```java
      var consul = new ConsulContainer(DockerImageName.parse("hashicorp/consul:1.15"));
      consul.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>consul</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/consul/
    maintainer: core
    example: |
      ```go
      consulContainer, err := consul.Run(context.Background(), "hashicorp/consul:1.15")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/consul
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Consul
    maintainer: core
    example: |
      ```csharp
      var consulContainer = new ConsulBuilder()
        .WithImage("consul:1.15")
        .Build();
      await consulContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Consul
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/consul/struct.Consul.html
    maintainer: community
    example: |
      ```rust
      use testcontainers_modules::{consul, testcontainers::runners::SyncRunner};

      let consul = consul::Consul::default().start().unwrap();
      let http_port = consul.get_host_port_ipv4(8500).unwrap();

      // do something with the started consul instance..
      ```
    installation: |
      ```bash
      cargo add -F consul --dev testcontainers-modules
      ```
description: |
  Consul is a service mesh and distributed key-value store.

  With the increasing popularity of Consul and config externalization, applications are now needing to source properties from Consul. This can prove challenging in the development phase without a running Consul instance readily on hand. This module solves integration testing with Consul. You can also use it to test how your application behaves with Consul by writing different test scenarios.
---
