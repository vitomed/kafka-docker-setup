TOPIC = "nlp"


ProducerConfig = {
    "bootstrap_servers": "localhost:9092",
    "client_id": "vitomed",
    "acks": "all"
}


ConsumerConfig = {
    "bootstrap_servers": "localhost:9092",
    "client_id": "vitomed",
}
