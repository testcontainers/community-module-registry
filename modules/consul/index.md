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
  - id: go
    url: https://golang.testcontainers.org/modules/consul/
    maintainer: core
    example: |
      ```go
      consulContainer, err := consul.RunContainer(ctx, testcontainers.WithImage("hashicorp/consul:1.15"))
      ```
description: |
  Consul is a service mesh and distributed key-value store.

  With the increasing popularity of Consul and config externalization, applications are now needing to source properties from Consul. This can prove challenging in the development phase without a running Consul instance readily on hand. This module solves integration testing with Consul. You can also use it to test how your application behaves with Consul by writing different test scenarios.
---