// read the KAFKA Brokers and KAFKA_TOPIC values from the local file config.js
const externalConfig = require('./config').config;

const { Kafka, logLevel } = require('kafkajs')

const kafka = new Kafka({
  clientId: 'my-app',
  brokers: externalConfig.KAFKA_BROKERS,
  logLevel: logLevel.INFO
})

// create a producer client on the Kafka Cluster
const producer = kafka.producer()


let messageCounter = 1;

const produceMessage = async (message) => {
    console.log(`Produce message ${message} to ${topic}`)
    await producer.connect()
    await producer.send({
      topic: topic,
      messages: [
        { key:  ""+messageCounter++, value: message },
        // ""+messageCounter++ is a lazy way of making sure that the value of key is a string
      ],
    })
    await producer.disconnect()
    console.log("Done Producing")
  }
  
const topic = externalConfig.KAFKA_TOPIC;


module.exports = {  produceMessage };