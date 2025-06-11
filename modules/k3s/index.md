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
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>k3s</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/k3s/
    maintainer: core
    example: |
      ```go
      k3sContainer, err := k3s.Run(context.Background(), "rancher/k3s:v1.27.1-k3s1")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/k3s
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
    installation: |
      ```bash
      dotnet add package Testcontainers.K3s
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/k3s/README.html
    maintainer: core
    example: |
      ```python
      with K3SContainer() as k3s:
          kube_config = k3s.config_yaml()
      ```
    installation: |
      ```bash
      pip install testcontainers[k3s]
  - id: nodejs
    url: https://node.testcontainers.org/modules/k3s/
    maintainer: core
    example: |
      ```javascript
      const container = await new K3sContainer("rancher/k3s:v1.31.2-k3s1").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/k3s --save-dev
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/k3s/struct.K3s.html
    maintainer: community
    example: |
      ```rust
      use std::env::temp_dir;

      use testcontainers_modules::{
          k3s::{K3s, KUBE_SECURE_PORT},
          testcontainers::{runners::SyncRunner, ImageExt},
      };

      let k3s_instance = K3s::default()
          .with_conf_mount(&temp_dir())
          .with_privileged(true)
          .with_userns_mode("host")
          .start()
          .unwrap();

      let kube_port = k3s_instance.get_host_port_ipv4(KUBE_SECURE_PORT);
      let kube_conf = k3s_instance
          .image()
          .read_kube_config()
          .expect("Cannot read kube conf");
      // use kube_port and kube_conf to connect and control k3s cluster
      ```
    installation: |
      ```bash
      cargo add -F k3s --dev testcontainers-modules
      ```
description: |
  K3s is a highly available, certified Kubernetes distribution designed for production workloads in unattended, resource-constrained, remote locations or inside IoT appliances.
---
