import memcache
conn2=memcache.Client(['192.168.1.143:11211'],debug=True,cache_cas=True)
result=conn2.gets('n')
print(result)
input('>>>')
conn2.cas('n',100)