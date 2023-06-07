---
title: WireMock
categories:
  - cloud
  - web
  - other
docs:
  - id: java
    url: https://github.com/wiremock/wiremock-testcontainers-java
    isThirdParty: true
    example: |
      ```java
        import org.junit.jupiter.api.*;
        import org.testcontainers.junit.jupiter.*;
        import org.wiremock.integrations.testcontainers.testsupport.http.*;

        import static org.assertj.core.api.Assertions.assertThat;

        @Testcontainers
        class WireMockContainerJunit5Test {

            @Container
            WireMockContainer wiremockServer = new WireMockContainer("2.35.0")
                    .withMapping("hello", WireMockContainerJunit5Test.class, "hello-world.json");

            @Test
            void helloWorld() throws Exception {
                String url = wiremockServer.getUrl("/hello");
                HttpResponse response = new TestHttpClient().get(url);
                assertThat(response.getBody())
                        .as("Wrong response body")
                        .contains("Hello, world!");
            }
        }
      ```
description: |
    This module allows provisioning the WireMock server as a standalone container within your unit test,
    based on [WireMock Docker](https://github.com/wiremock/wiremock-docker).

    WireMock is a popular open-source tool for API mock testing with over 5 million downloads per month.
    It can help you to create stable test and development environments,
    isolate yourself from flakey 3rd parties and simulate APIs that don’t exist yet.
    WireMock has a rich matching system, allowing any part of an incoming request
    to be matched against complex and precise criteria. 
    [Read more about WireMock](https://wiremock.org/docs/)
---
