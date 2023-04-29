from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['localhost:29092', 'localhost:29093', 'localhost:29094'])

topic = 'test-topic'

# ====   First Message ======= 

# Asynchronous by default
future = producer.send(topic, b'Message from Python')

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

# Successful result returns assigned partition and offset
print ('message published to Kafka topic')
print('topcic: '+ record_metadata.topic)
print('partition: '+ str(record_metadata.partition))
print('message offset after publication: ' + str(record_metadata.offset))


# ====  Second Message (with key and value) ======= 

# produce keyed messages to enable hashed partitioning
producer.send(topic, key=b'foo', value=b'bar')
print ("Done one nore")


# ====  Bunch of messages in parallel ======= 

# produce asynchronously
for i in range(15):
    message = 'More news from Python - sequence number ' + str(i) 
    producer.send(topic, str.encode(message))

print('just published 15 messages (or at least started the asynchronous commands to do so) ')


# ====  Produce messages with callbacks to handle publication events ======= 

def on_send_success(record_metadata):
    print('callback reports: success in publishing message')
    print('topcic: '+ record_metadata.topic)
    print('partition: '+ str(record_metadata.partition))
    print('message offset after publication: ' + str(record_metadata.offset))

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception

# produce asynchronously with callbacks
producer.send(topic, b'raw_bytes').add_callback(on_send_success).add_errback(on_send_error)

# block until all async messages are sent - here asynchronous behavior is synchronized
producer.flush()

# configure multiple retries
producer = KafkaProducer(retries=5)