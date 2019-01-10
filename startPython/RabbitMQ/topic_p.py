import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.143'))
channel = connection.channel()
channel.exchange_declare(exchange='topic_log', exchange_type='topic')
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
