const { Kafka, logLevel } = require('kafkajs')

const externalConfig = require('./config').config;

const kafka = new Kafka({
    clientId: 'my-app',
    brokers: externalConfig.KAFKA_BROKERS,
    logLevel: logLevel.INFO
  })
  

const CONSUMER_GROUP_ID = "iot-platform-consumer"+new Date().getTime() // only use a static consumer_group_id once all messages are persisted in the IoT Platform microservice
const topic = externalConfig.KAFKA_TOPIC;

let messageHandler // a reference to a function that wants to handle each message received
const setMessageHandler = function (messageHandlingFunction) {
    messageHandler = messageHandlingFunction
}

const initializeConsumer = async () => {
    const consumer = kafka.consumer({ groupId: CONSUMER_GROUP_ID })
  
    await consumer.connect()
    await consumer.subscribe({ topic: topic, fromBeginning: true })
  
    await consumer.run({
      eachMessage: async ({ topic, partition, message }) => {
        const prefix = `${topic}[${partition} | ${message.offset}] / ${message.timestamp}`
        console.log(`- ${prefix} ${message.key}#${message.value}`)
        if (messageHandler) messageHandler(message)
      },
    })
  }
  
module.exports = { setMessageHandler, initializeConsumer };