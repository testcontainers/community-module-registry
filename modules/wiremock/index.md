---
title: WireMock
categories:
  - cloud
  - web
officialPartner:
  name: WireMock
  url: https://wiremock.org/
docs:
  - id: java
    url: https://github.com/wiremock/wiremock-testcontainers-java
    maintainer: official
    example: |
      ```java
      WireMockContainer wiremockServer = new WireMockContainer("2.35.0")
                .withMapping("hello", WireMockContainerJunit5Test.class, "hello-world.json");
      wiremockServer.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.wiremock.integrations.testcontainers</groupId>
          <artifactId>wiremock-testcontainers-module</artifactId>
          <version>1.0-alpha-13</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: nodejs
    url: https://github.com/wiremock/wiremock-testcontainers-node
    maintainer: official
    example: |
      ```js
      import { WireMockContainer } from "wiremock-testcontainers-node";
      const container = await new WireMockContainer()
        .withMapping("./mapping.json")
        .withExposedPorts(8080)
        .start();
      ```
    installation: |
      ```bash
      npm install @wiremock/wiremock-testcontainers-node --save-dev
      ```
  - id: go
    url: https://github.com/wiremock/wiremock-testcontainers-go
    maintainer: official
    example: |
      ```golang
       ctx := context.Background()
       container, err := RunContainer(ctx,
         WithImage("wiremock/wiremock:2.35.0-1"),
         WithMappingFile("hello", filepath.Join("testdata", "hello-world.json")),
       )
       if err != nil {
         t.Fatal(err)
       }
       t.Cleanup(func() {
         if err := container.Terminate(ctx); err != nil {
         t.Fatalf("failed to terminate container: %s", err)
         }
       })
      ```
    installation: |
      ```bash
      go get github.com/wiremock/wiremock-testcontainers-go
      ```
  - id: python
    url: https://wiremock.readthedocs.io/en/latest/testcontainers/
    maintainer: official
    example: |
      ```python
      @pytest.fixture(scope="session") # (1)
      def wm_server():
        with wiremock_container(secure=False) as wm:

          Config.base_url = wm.get_url("__admin") # (2)
          Mappings.create_mapping(
            Mapping(
              request=MappingRequest(method=HttpMethods.GET, url="/hello"),
              response=MappingResponse(status=200, body="hello"),
              persistent=False,
            )
          ) # (3)
          yield wm
      ```
    installation: |
      ```bash
      pip install wiremock
      ```
description: |
    This module allows provisioning the WireMock server as a standalone container within your tests,
    based on [WireMock Docker](https://github.com/wiremock/wiremock-docker).

    WireMock is a popular open-source tool for API mock testing with over 5 million downloads per month.
    It can help you to create stable test and development environments,
    isolate yourself from flakey 3rd parties and simulate APIs that don’t exist yet.
    WireMock has a rich matching system, allowing any part of an incoming request
    to be matched against complex and precise criteria.

    Read more:
     - [WireMock Documentation](https://wiremock.org/docs/)
     - [WireMock and Testcontainers](https://wiremock.org/docs/solutions/testcontainers/)
---
