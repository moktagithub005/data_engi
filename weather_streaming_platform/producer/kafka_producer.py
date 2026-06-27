from kafka import KafkaProducer
import json
from configs.kafka_config import(
    BOOTSTRAP_SERVER,
    RAW_TOPIC
)
# CREATE KAFKA PRODUCER
producer=KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVER,
    value_serializer=lambda value:
      json.dumps(value).encode("utf-8")
)


def publish_event(event,key=None):
    future=producer.send(
        topic=RAW_TOPIC,
        key=key.encode("utf-8") if key else None,
        value=event
   )
    return future

def publish_and_confirmation(event,key=None):
    future=publish_event(event,key)
    metadata=future.get(timeout=10)
    return metadata

def close():
    producer.flush()
    producer.close()
