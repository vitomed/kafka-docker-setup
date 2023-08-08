from random import choice

from kafka import KafkaProducer

from .config import ProducerConfig


class MyKafkaProducer:
    TOPIC = "nlp"

    def __init__(self):
        self.producer = KafkaProducer(**ProducerConfig)

    def produce(self, product: bytes, user_id, topic=None, ):
        if topic is None:
            topic = self.TOPIC

        self.producer.send(topic, product)

    def flush(self):
        self.producer.flush()


if __name__ == '__main__':
    producer = MyKafkaProducer()
    # Produce data by selecting random values from these lists.
    user_ids = ['eabara', 'jsmith', 'sgarcia', 'jbernard', 'htanaka', 'awalther']
    products = ['book', 'alarm clock', 't-shirts', 'gift card', 'batteries']

    count = 0
    for _ in range(10):
        user_id = choice(user_ids)
        product = choice(products)
        producer.produce(product.encode("utf-8"), user_id,)
        count += 1

    # Block until the messages are sent.
    # producer.poll(10000)
    producer.flush()
