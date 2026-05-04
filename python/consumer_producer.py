from kafka import KafkaConsumer, KafkaProducer
from const import *

consumer = KafkaConsumer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])
producer = KafkaProducer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])

consumer.subscribe(['topic-temperature'])

readings = []

print('Listening on topic-temperature...')

for msg in consumer:
    temperature = float(msg.value.decode())
    readings.append(temperature)
    print('Received temperature: ' + str(temperature))

    if len(readings) > 10:
        readings.pop(0)

    average = round(sum(readings) / len(readings), 2)
    producer.send('topic-average', value=str(average).encode())
    producer.flush()
    print('Forwarded average: ' + str(average))
