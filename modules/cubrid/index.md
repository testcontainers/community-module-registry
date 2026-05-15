---
title: CUBRID
categories:
  - relational-database
officialPartner:
  name: CUBRID
  url: https://www.cubrid.org
docs:
  - id: java
    url: https://github.com/CUBRID/testcontainers-cubrid
    maintainer: official
    example: |
      ```java
      var cubrid = new CubridContainer("cubrid/cubrid:11.4");
      cubrid.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.cubrid</groupId>
          <artifactId>testcontainers-cubrid</artifactId>
          <version>0.1.0</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  CUBRID is an open-source relational database management system optimised for web and OLTP applications, with built-in high availability and online incremental backup.
---
