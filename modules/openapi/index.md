---
title: OpenAPI
categories:
  - cloud
docs:
  - id: java
    url: https://github.com/gcatanese/openapi-testcontainers
    maintainer: community
    example: |
      ```java
          @ClassRule
          public static GenericContainer container = new GenericContainer(
            new ImageFromDockerfile("my-test-cont", false)
                    .withFileFromFile("openapi.yaml", new File(OPENAPI_FILE))
                    .withFileFromFile("Dockerfile", new File("Dockerfile"))
            )
            .withExposedPorts(8080);      
      ```
    installation: |
      ```xml
      <dependency>
        <groupId>org.testcontainers</groupId>
        <artifactId>testcontainers</artifactId>
        <version>1.17.3</version>
        <scope>test</scope>
      </dependency>
      ```
description: |
  The OpenAPI Testcontainers extension allows developers to create on-the-fly a lightweight Test Container from an
  [OpenAPI](https://spec.openapis.org/) specification file. The API container is loaded when the Junit tests start and can be used to mock the different endpoints and payloads.

  Read more on [openapi-testcontainers](https://github.com/gcatanese/openapi-testcontainers) and checkout the [demo](https://github.com/gcatanese/openapi-testcontainers-demo).
---
