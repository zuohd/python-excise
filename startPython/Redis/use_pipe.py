import redis

pool=redis.ConnectionPool(host='192.168.1.143',port=6379)
r=redis.Redis(connection_pool=pool)

pipe=r.pipeline(transaction=True)
r.set('hello','world')
r.set('blog','https//zuohd.github.io/')
pipe.execute()