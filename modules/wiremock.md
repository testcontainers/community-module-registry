---
title: WireMock
categories:
  - cloud
  - web
docs:
  - id: java
    url: https://github.com/wiremock/wiremock-testcontainers-java
    isThirdParty: true
    example: |
      ```java
      WireMockContainer wiremockServer = new WireMockContainer("2.35.0")
                .withMapping("hello", WireMockContainerJunit5Test.class, "hello-world.json");
      wiremockServer.start();                
      ```
description: |
    This module allows provisioning the WireMock server as a standalone container within your tests,
    based on [WireMock Docker](https://github.com/wiremock/wiremock-docker).

    WireMock is a popular open-source tool for API mock testing with over 5 million downloads per month.
    It can help you to create stable test and development environments,
    isolate yourself from flakey 3rd parties and simulate APIs that don’t exist yet.
    WireMock has a rich matching system, allowing any part of an incoming request
    to be matched against complex and precise criteria. 
    [Read more about WireMock](https://wiremock.org/docs/)
---
