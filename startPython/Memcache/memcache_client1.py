import memcache
conn1=memcache.Client(['192.168.1.143:11211'],debug=True,cache_cas=True)
conn1.set('n',9)
result=conn1.gets('n')
print(result)
input('>>>')
conn1.cas('n',99)
