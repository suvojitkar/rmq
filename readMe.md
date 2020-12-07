- Install rmq
- Install pika: pip3 install pika
- start rmq: /usr/local/sbin/rabbitmq-server start
- stop rmq: /usr/local/sbin/rabbitmqctl stop
- Run receive.py: python3 receive.py
- run send.py: python3 send.py

WebUI: 
url: http://localhost:15672/
username/pass: guest/guest

protocol:
AMPQ: Advanced Message Queuing Protocol

More details: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

RoundRobin: 
https://www.youtube.com/watch?v=-jFGYDfWkXI
