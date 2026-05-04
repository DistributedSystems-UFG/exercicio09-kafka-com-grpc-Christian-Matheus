from kafka import KafkaProducer
from const import *
import time
import random

producer = KafkaProducer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])

print('Starting temperature sensor...')

while True:
    temperature = round(random.uniform(20.0, 35.0), 2)
    msg = str(temperature)
    producer.send('topic-temperature', value=msg.encode())
    producer.flush()
    print('Sent temperature: ' + msg)
    time.sleep(3)
