---
title: OpenFGA
categories:
  - other
docs:
  - id: java
    url: https://java.testcontainers.org/modules/openfga/
    maintainer: core
    example: |
      ```java
      var openfga = new OpenFGAContainer("openfga/openfga:v1.4.3");
      openfga.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/openfga/
    maintainer: core
    example: |
      ```go
      openfgaContainer, err := openfga.RunContainer(ctx, testcontainers.WithImage("openfga/openfga:v1.5.0"))
      ```
description: |
  OpenFGA is an open-source authorization solution that allows developers to build granular access control using an easy-to-read modeling language and friendly APIs.
---