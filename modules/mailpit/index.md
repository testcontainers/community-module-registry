---
title: Mailpit
categories:
  - other
docs:
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/mailpit/README.html
    maintainer: core
    example: |
      ```python
      with MailpitContainer(image = "axllent/mailpit:v1.21") as mailpit:
          host_ip = mailpit.get_container_host_ip()
          host_port = mailpit.get_exposed_smtp_port()
          server = smtplib.SMTP(
              mailpit.get_container_host_ip(),
              mailpit.get_exposed_smtp_port(),
          )
         code, _ = server.login("any", "auth")
      ```
    installation: |
      ```bash
      pip install testcontainers[mailpit]
      ```
description: |
  Mailpit is a small, fast, low memory, zero-dependency, multi-platform email testing tool & API for developers.
---
