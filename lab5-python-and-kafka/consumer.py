from kafka import KafkaConsumer

topic = 'test-topic'
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(topic,
                       #  group_id='my-group', # consumer group; when set, for that value each message is consumed just once 
                         bootstrap_servers=['localhost:29092', 'localhost:29093', 'localhost:29094'],
                         auto_offset_reset='earliest'  # Indicates whether to consume only new messages or all messages (from the very first) Default: ‘latest’, alternati.      
                         )

print('consume messages from the topic %s ' %(topic))
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))

# the program will keep polling for messages until interrupted