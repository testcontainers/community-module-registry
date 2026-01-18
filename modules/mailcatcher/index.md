---
title: MailCatcher
categories:
  - other
docs:
  - id: java
    url: https://github.com/martinellich/testcontainers-mailcatcher
    maintainer: community
    example: |
      ```java
      var mailCatcher = new MailCatcherContainer();
      mailCatcher.start();
      ```      
description: |
  MailCatcher runs a super simple SMTP server which catches any message sent to it to display in a web interface.
---

