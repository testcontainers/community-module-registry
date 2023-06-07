---
title: Plain Git Server
categories:
  - git
docs:
  - id: java
    url: https://github.com/sparsick/testcontainers-git
    isThirdParty: true
    example: |
      ```java
      var gitServer = 
            new GitServerContainer(DockerImageName.parse("rockstorm/git-server:2.38"))
                    .withGitRepo("testRepo") // overwrite the default git repository name
                    .withGitPassword("12345"); // overwrite the default git password
      gitServer.start();
      ```
description: |
   Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. 
---