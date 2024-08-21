---
title: Alfresco
categories:
  - other
docs:
  - id: java
    url: https://github.com/AlfrescoLabs/alfresco-testcontainers
    maintainer: community
    example: |
      ```java
      var alfresco = new AlfrescoContainer(DockerImageName.parse("alfresco/alfresco-content-repository-community:23.2.1"));
      alfresco.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.alfresco</groupId>
          <artifactId>alfresco-testcontainers</artifactId>
          <version>0.8.0</version>
      </dependency>
      ```
description: |
  Alfresco is a scalable, flexible, and extensible open-source software suite for content management and collaboration applications licensed under LGPLv3 and powered by open standards.
---