---
title: Gradle Plugin
categories:
  - other
docs:
  - id: java
    url: https://github.com/regulskimichal/testcontainers-gradle-plugin
    maintainer: community
    example: |
      ```kotlin
      import org.testcontainers.containers.JdbcDatabaseContainer
      import org.testcontainers.gradle.DatabaseType
      import org.testcontainers.gradle.getContainer

      // 1. Define container
      testcontainers {
          jdbcContainer("postgres", DatabaseType.POSTGRESQL) {
              image("postgres:18-alpine")
              databaseName("testdb")
              username("user")
              password("pass")
              portMapping(5432)
          }
      }

      // 2. Use container in a custom task
      tasks.register("printDbInfo") {
          dependsOn("startPostgresContainer")
          usesService(testcontainers.service)

          val dbProvider = testcontainers.getContainer<JdbcDatabaseContainer<*>>("postgres")

          doFirst {
              val db = dbProvider.get()
              logger.warn(
                  """
                  SUCCESSFULLY CONFIGURED POSTGRES CONTAINER!
                  JDBC URL: ${db.jdbcUrl}
                  Username: ${db.username}
                  Password: ${db.password}""".trimIndent()
              )
          }
      }
      ```
    installation: |
      ```kotlin
      plugins {
          id("io.github.regulskimichal.testcontainers") version "0.2.0"
      }

      // additional configuration, add modules you want to use in the build process
      dependencies {
          "testcontainersClasspath"("org.testcontainers:testcontainers-postgresql:2.0.5")
      }
      ```
description: |
  A minimal, framework-agnostic Gradle plugin that manages container lifecycles for build-time tasks (such as code generation, database migrations, schema inspection, or integration testing) using Testcontainers.
---
