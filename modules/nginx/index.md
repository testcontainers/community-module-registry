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
description: |
  Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.
---