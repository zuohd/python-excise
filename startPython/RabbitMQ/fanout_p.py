import pika
connection=pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.143'))
channel=connection.channel()
channel.exchange_declare(exchange='logs',exchange_type='fanout')
channel.basic_publish(exchange='logs',routing_key='',body='Hello Worlduuuuu')
connection.close()