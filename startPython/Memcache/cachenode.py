import binascii

def cmemcache_hash(key):
    return ((((binascii.crc32(key) & 0xffffffff) >> 16) & 0x7fff) or 1)


result = cmemcache_hash(bytes('k', encoding='utf-8'))
print(result)
