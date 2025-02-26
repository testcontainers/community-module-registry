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
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>openfga</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/openfga/
    maintainer: core
    example: |
      ```go
      openfgaContainer, err := openfga.Run(context.Background(), "openfga/openfga:v1.5.0")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/openfga
      ```
description: |
  OpenFGA is an open-source authorization solution that allows developers to build granular access control using an easy-to-read modeling language and friendly APIs.
---
