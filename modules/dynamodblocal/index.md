---
title: DynamoDB Local
categories:
  - nosql-database
docs:
  - id: java
    url: https://github.com/dahyvuun/testcontainers-dynamodblocal
    maintainer: community
    example: |
      ```java
      var container = new DynamoDBLocalContainer("amazon/dynamodb-local:2.2.1");
      container.start();
      ```
description: |
  Amazon DynamoDB Local is a downloadable version of DynamoDB that lets you develop and test applications without accessing the DynamoDB web service.
---
