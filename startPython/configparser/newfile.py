import configparser
config=configparser.ConfigParser()
config.read('file.conf',encoding='utf-8')
config.add_section("node1")
config.add_section("node2")
config.write(open('file.conf','w'))