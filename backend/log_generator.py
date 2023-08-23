import logging
import pika
import random
import time

# connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
# channel = connection.channel()
# channel.exchange_declare(exchange="logs", exchange_type="fanout")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

while True:
    log_level = random.choice(["DEBUG", "INFO", "WARNING", "ERROR"])
    log_message = f" {random.random} log message with level {log_level}"
    logging.info(log_message)
    channel.basic_publish(exchange="logs", routing_key="", body=log_message)
    time.sleep(random.uniform(  0.5, 2.0))

connection.close()
