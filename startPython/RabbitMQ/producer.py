import pika

connection=pika.BlockingConnection(pika.ConnectionParameters('192.168.1.143'))
channel=connection.channel()
channel.queue_declare(queue='hello',durable=True)
channel.basic_publish(exchange='',routing_key='hello',body='Hello World!',\
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      ))

connection.close()