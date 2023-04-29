# Lab - Programmatic interaction with Apache Kafka from Java

- [Lab - Programmatic interaction with Apache Kafka from Java](#lab---programmatic-interaction-with-apache-kafka-from-java)
  - [Java interacting with Apache Kafka](#java-interacting-with-apache-kafka)
    - [Producing to test-topic in Java](#producing-to-test-topic-in-java)
    - [Consuming from test-topic in Java](#consuming-from-test-topic-in-java)

In the labs 3 and 5, you have produced and consumed messages from Node and Python respectively. In this lab, you will also produce and consume messages in a programmatic way, from Java this time. You will use the Apache Kafka platform that you used in earlier labs as well as the Java run time environment that is also part of the Gitpod workspace. 

## Java interacting with Apache Kafka

Apache Kafka itself is written in Java and Scala and it runs on JVMs. Kafka's native API was written in Java as well. 


The sources for this part of the lab are in the directory *lab6-java-and-kafka* directory.

cd enterprisemessageplatform

build project:

mvn clean package

builds JAR file: lab6-java-and-kafka/enterprisemessageplatform/target/enterprisemessageplatform-1.0-SNAPSHOT-jar-with-dependencies.jar

then run:

java -cp target/enterprisemessageplatform-1.0-SNAPSHOT-jar-with-dependencies.jar com.mycomp.emp.App

### Producing to test-topic in Java

java -cp target/enterprisemessageplatform-1.0-SNAPSHOT-jar-with-dependencies.jar com.mycomp.emp.Producer



### Consuming from test-topic in Java




java -cp target/enterprisemessageplatform-1.0-SNAPSHOT-jar-with-dependencies.jar com.mycomp.emp.Consumer

see: https://www.conduktor.io/kafka/complete-kafka-consumer-with-java/