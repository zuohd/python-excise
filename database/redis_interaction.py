import redis

# connect

rdb = redis.StrictRedis(host="localhost", port=6379)  # if configured password ,need to pass it


# rdb.set("a1","good")
result=rdb.get("a1")
print(result.decode("utf8"))
# rdb.lpush("a2",[1,2,3])

pipe=rdb.pipeline() # decrease tcp connection from client to redis server with pipeline
pipe.set("c1","hello")
pipe.set("c2","world")
pipe.execute()