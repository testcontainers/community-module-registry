---
title: Nginx
categories:
  - web
docs:
  - id: java
    url: https://java.testcontainers.org/modules/nginx/
    maintainer: core
    example: |
      ```java
      var nginx = new NginxContainer<>(DockerImageName.parse("nginx:1.23.4-alpine"));
      nginx.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>nginx</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/nginx/README.html
    maintainer: community
    example: |
      ```python
      with NginxContainer() as nginx:
          url = f"http://{nginx.get_container_host_ip()}:{nginx.get_exposed_port(nginx.port)}/"
      ```
    installation: |
      ```bash
      pip install testcontainers[nginx]
      ```
description: |
  Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.
---
