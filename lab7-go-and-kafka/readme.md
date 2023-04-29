# Lab - Programmatic interaction with Apache Kafka from Go

- [Lab - Programmatic interaction with Apache Kafka from Go](#lab---programmatic-interaction-with-apache-kafka-from-go)
  - [Go interacting with Apache Kafka](#go-interacting-with-apache-kafka)
    - [Producing to test-topic in Go](#producing-to-test-topic-in-go)
    - [Consuming messages from test-topic in Go](#consuming-messages-from-test-topic-in-go)
    - [Resources](#resources)

In the labs 3, 5 and 6, you have produced and consumed messages from Node, Python and Java respectively. In this lab, you will also produce and consume messages in a programmatic way, from Go. You will use the Apache Kafka platform that you used in earlier labs as well as the Go(lang) run time environment that is also part of the Gitpod workspace. 

## Go interacting with Apache Kafka

Several libraries are available for interaction with Apache Kafka from Go. See [this list on the Apache Kafka website](https://cwiki.apache.org/confluence/display/KAFKA/Clients#Clients-Go(AKAgolang)). Then there is also [Franz-Go](https://github.com/twmb/franz-go) with 1K stars on GitHub. The most popular seems to be [Sarama](https://github.com/Shopify/sarama) (10K stars). We will use that library in this lab: "Package sarama is a pure Go client library for dealing with Apache Kafka (versions 0.8 and later). It includes a high-level API for easily producing and consuming messages, and a low-level API for controlling bytes on the wire when the high-level API is insufficient. Usage examples for the high-level APIs are provided inline with their full documentation."

The sources for this part of the lab are in the directory *lab7-go-and-kafka* directory.

### Producing to test-topic in Go

To produce messages, use either the AsyncProducer or the SyncProducer. The AsyncProducer accepts messages on a channel and produces them asynchronously in the background as efficiently as possible; it is preferred in most cases. The SyncProducer provides a method which will block until Kafka acknowledges the message as produced. This can be useful but comes with two caveats: it will generally be less efficient, and the actual durability guarantees depend on the configured value of `Producer.RequiredAcks`. There are configurations where a message acknowledged by the SyncProducer can still sometimes be lost.

In directory `lab7-go-and-kafka\go-producer`

run

```
 go run main.go
```


### Consuming messages from test-topic in Go

To consume messages, use Consumer or Consumer-Group API.


### Resources

Wiki on sarana Go library for Kafka: https://github.com/Shopify/sarama/wiki

Regular user documentation is provided via godoc: https://godoc.org/github.com/Shopify/sarama

