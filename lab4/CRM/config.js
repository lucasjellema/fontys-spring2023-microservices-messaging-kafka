//Configuration Details for the Kafka Brokers and Topic
const config = {
    // If you added kafka-1, kafka-2 and/or kafka-3 to the hosts file mapped to the IP address of the Docker Host machine, then you can work with these Broker Endpoints
    KAFKA_BROKERS: ['localhost:29092', 'localhost:29093', 'localhost:29094']
    , KAFKA_TOPIC: "connection-mandates-topic"
};
module.exports = { config };