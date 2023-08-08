from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from dataclasses import asdict

from confluent_kafka import OFFSET_BEGINNING
from kafka import KafkaConsumer

from app.config import TOPIC, ConsumerConfig


class MyKafkaConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(**ConsumerConfig)

    def subscribe(self, *args, **kwargs):
        self.consumer.subscribe(*args, **kwargs)


if __name__ == '__main__':
    # Create Consumer instance
    consumer = MyKafkaConsumer()

    # Subscribe to topic
    consumer.subscribe([TOPIC])

    # Poll for new messages from Kafka and print them.
    try:
        for message in consumer.consumer:
            print(message)
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.consumer.close()
