---
title: Docker MCP Gateway
categories:
  - other
docs:
  - id: java
    url: https://java.testcontainers.org/modules/docker_mcp_gateway/
    maintainer: core
    example: |
      ```java
      DockerMcpGatewayContainer gateway = new DockerMcpGatewayContainer("docker/mcp-gateway:latest")
        .withServer("curl", "curl")
        .withServer("brave", "brave_local_search", "brave_web_search")
        .withServer("github-official", Collections.singletonList("add_issue_comment"))
        .withSecret("brave.api_key", "test_key")
        .withSecrets(Collections.singletonMap("github.personal_access_token", "test_token"));

      gateway.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/dockermcpgateway/
    maintainer: core
    example: |
      ```go
      ctr, err := dmcpg.Run(
          ctx, "docker/mcp-gateway:latest",
          dmcpg.WithTools("curl", []string{"curl"}),
          dmcpg.WithTools("duckduckgo", []string{"fetch_content", "search"}),
          dmcpg.WithTools("github-official", []string{"add_issue_comment"}),
      )
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/dockermcpgateway
      ```
description: |
    The MCP Gateway is Docker's open-source enterprise-ready solution for orchestrating and managing
    Model Context Protocol (MCP) servers securely across development and production environments.
---
