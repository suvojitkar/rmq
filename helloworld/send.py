__author__ = "Suvojit Kar"

import pika
# establish a connection with RabbitMQ server
# use IP or name in case the broker is a different machine
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# create a queue named hello
# If queue doesnt exist, it creates a new one
channel.queue_declare(queue='hello')

# In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange
# routing_key should contain the name of the queue to which message should be passed to using exchange policy(default in this case)
# body is the message to be send
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

# Before exiting the program we need to make sure the network buffers were flushed and our message was actually delivered to RabbitMQ. 
# We can do it by gently closing the connection.
connection.close()
