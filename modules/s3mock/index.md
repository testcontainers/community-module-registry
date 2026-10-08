---
title: S3Mock
categories:
  - cloud
  - web
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
  - id: go
    url: https://golang.testcontainers.org/modules/s3mock/
    maintainer: core
    example: |
      ```go
      s3mockContainer, err := s3mock.Run(context.Background(), "adobe/s3mock:3.9")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/s3mock
      ```

  - id: nodejs
    url: https://node.testcontainers.org/modules/s3mock/
    maintainer: core
    example: |
      ```javascript
      const container = await new S3MockContainer("adobe/s3mock:5.1.0").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/s3mock --save-dev
      ```
description: |
    S3Mock is a popular open-source library that allows mock testing against many S3 APIs.

    Read more:
     - [S3Mock Documentation](https://github.com/adobe/S3Mock/blob/main/README.md)
---
