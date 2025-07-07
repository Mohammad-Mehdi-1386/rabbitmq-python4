import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
ch = connection.channel()

ch.queue_declare("one")
ch.basic_publish(exchange="" , routing_key="one" ,body="Hello World")
print("Message Sent...")

connection.close()