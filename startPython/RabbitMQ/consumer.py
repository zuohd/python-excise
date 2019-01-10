import pika
connnection=pika.BlockingConnection(pika.ConnectionParameters('192.168.1.143'))
channel=connnection.channel()
channel.queue_declare(queue='hello',durable=True)

def callback(ch,method,properties,body):
    print("[x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,queue='hello',no_ack=True)
channel.start_consuming()