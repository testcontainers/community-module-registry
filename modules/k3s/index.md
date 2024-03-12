---
title: K3S
categories:
  - other
docs:
  - id: java
    url: https://java.testcontainers.org/modules/k3s/
    maintainer: core
    example: |
      ```java
      var k3s = new K3sContainer(DockerImageName.parse("rancher/k3s:v1.21.3-k3s1"));
      k3s.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/k3s/
    maintainer: core
    example: |
      ```go
      k3sContainer, err := k3s.RunContainer(ctx, testcontainers.WithImage("rancher/k3s:v1.27.1-k3s1"))
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.K3s
    maintainer: core
    example: |
      ```csharp
      var k3sConainter = new K3sBuilder()
        .WithImage("rancher/k3s:v1.26.2-k3s1")
        .Build();
      await k3sConainter.StartAsync();
      ```
description: |
  K3s is a highly available, certified Kubernetes distribution designed for production workloads in unattended, resource-constrained, remote locations or inside IoT appliances.
---