import time
import logging



from producer.weather_service import get_weather_event

from producer.kafka_producer import (
    publish_and_confirm,
    close,
)

def run_weather_producer():
    print(" run_weather_producer() started")
    while True:
        print("Inside while loop")
        try:
            print("Calling get_weather_event()")
            event=get_weather_event()
            print("Weather Event Created Successfully")
            print(event)
            metadata=publish_and_confirm(
                event,
                key=event["city"]
            )
            logging.info(
                f"""
published sucessfully
Topic: {metadata.topic}
Partition: {metadata.partition}
Offset: {metadata.offset}
"""
     )
        except Exception as e:
            logging.exception(
                f"producer Error:{e}"
            )
        finally:
            time.sleep(30)

if __name__ == "__main__":

    try:

        run_weather_producer()

    except KeyboardInterrupt:

        logging.info(

            "Producer Stopped by User."
        )

    finally:

        close()

        

