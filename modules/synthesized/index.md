---
title: Synthesized
categories:
  - relational-database
  - other
officialPartner:
  name: Synthesized
  url: https://synthesized.io
docs:
  - id: java
    url: https://docs.synthesized.io/tdk/latest/user_guide/integrations/testcontainers
    maintainer: official
    example: |
      ```java
      //Input JdbcDatabaseContainer: empty database with schema input
      PostgreSQLContainer<?> input = new PostgreSQLContainer<>("postgres:15-alpine")
          .withNetwork(network);

      //Output JdbcDatabaseContainer: output database with generated data output
      PostgreSQLContainer<?> output = new PostgreSQLContainer<>("postgres:15-alpine")
          .withNetwork(network);
      
      String config = """
              default_config:
                mode: GENERATION
                target_row_number: 10
              global_seed: 42
              """

      new SynthesizedTDK(SynthesizedTDK.DEFAULT_IMAGE_NAME)
          .transform(input, output, config);
      ```
description: |
  Synthesized Test Data Kit (TDK) is a DevOps’ best friend for database masking and generation. Forget about
  hacky masking and seeding scripts that can easily leak PII or produce inaccurate results. You can plug it 
  in into your CI/CD pipeline or use it as a command-line tool.
---
