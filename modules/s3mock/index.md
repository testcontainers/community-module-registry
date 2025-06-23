---
title: S3Mock
categories:
  - cloud
  - web
officialPartner:
  name: Adobe
  url: https://adobe.com/
docs:
  - id: java
    url: https://github.com/adobe/S3Mock/tree/main/testsupport/testcontainers
    maintainer: official
    example: |
      ```java
      S3MockContainer s3Mock = S3MockContainer("4.5.0")
      s3Mock.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>com.adobe.testing</groupId>
          <artifactId>s3mock-testcontainers</artifactId>
          <version>4.5.0</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
    S3Mock is a popular open-source library that allows mock testing against many S3 APIs.

    Read more:
     - [S3Mock Documentation](https://github.com/adobe/S3Mock/blob/main/README.md)
---
