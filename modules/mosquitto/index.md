---
title: Mosquitto
categories:
  - message-broker
docs:
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/mosquitto/README.html
    maintainer: core
    example: |
      ```python
      with MosquittoContainer(image = "eclipse-mosquitto:2.0.20") as mosquitto_broker:
         mqtt_client = mosquitto_broker.get_client()
      ```
    installation: |
      ```bash
      pip install testcontainers[mosquitto]
      ```
description: |
  Eclipse Mosquitto is an open source message broker which implements MQTT version 5, 3.1.1 and 3.1.
---
