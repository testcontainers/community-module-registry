---
title: IBM MQ
categories:
  - message-broker
docs:
  - id: java
    url: https://github.com/ibm-messaging/mq-jms-spring/
    maintainer: official
    example: |
      ```java
      import com.ibm.mq.testcontainers.MQContainer;

      var mqContainer = new MQContainer(MQContainer.DEFAULT_IMAGE)
          .acceptLicense();

      ```
    installation: |
      ```xml
      <dependency>
          <groupId>com.ibm.mq</groupId>
          <artifactId>mq-java-testcontainer</artifactId>
          <version>1.21.2</version>
          <scope>test</scope>
      </dependency>
      ```

description: |
  IBM MQ provides a universal messaging backbone with robust connectivity for flexible and reliable messaging for applications and the integration of existing IT assets.
---
