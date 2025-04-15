---
title: Xunit
categories:
  - test-framework
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Xunit
    maintainer: core
    example: |
      ```csharp
      // Inherit from either the `ContainerTest` or `ContainerFixture` class, set up your
      // container instance in `Configure(TContainerBuilder)`, and access the running
      // container in your test method using the `Container` property. The module handles
      // creating, starting, and disposing of the container instances in the background.

      public sealed partial class RedisContainerTest(ITestOutputHelper testOutputHelper)
        : ContainerTest<RedisBuilder, RedisContainer>(testOutputHelper)
      {
        protected override RedisBuilder Configure(RedisBuilder builder)
        {
          return builder.WithImage("redis:7.0");
        }

        [Fact]
        public async Task Test1()
        {
          _ = Container.GetConnectionString();
        }
      }
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Xunit
      ```
description: |
  The Testcontainers.Xunit package simplifies writing tests with containers in xUnit.net. By leveraging xUnit.net's shared context, this package automates the setup and teardown of test resources, creating and disposing of containers as needed. This reduces repetitive code and avoids common patterns that developers would otherwise need to implement repeatedly.

  You can read full example and docs here: https://dotnet.testcontainers.org/test_frameworks/xunit_net/.
---
