---
title: DynamoDB
categories:
  - nosql-database
docs:
  - id: go
    url: https://github.com/abhirockzz/dynamodb-local-testcontainers-go
    maintainer: community
    example: |
      ```go
      dynamodbLocalContainer, err := dynamodblocal.RunContainer(context.Background(), testcontainers.WithImage("amazon/dynamodb-local:2.2.1"))
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.DynamoDb
    maintainer: core
    example: |
      ```csharp
      var dynamoDbContainer = new DynamoDbBuilder()
        .WithImage("amazon/dynamodb-local:1.21.0")
        .Build();
      await dynamoDbContainer.StartAsync();
      ```
description: |
  Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. 

  [DynamoDB local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) is the downloadable version of Amazon DynamoDB that can be used to develop and test applications without accessing the DynamoDB web service. You can [run DynamoDB locally on your computer](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html) in multiple ways, including a Docker container.
---
