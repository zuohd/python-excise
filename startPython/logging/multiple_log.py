import logging
file1=logging.FileHandler('log1.log','a')
fmt1=logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
file1.setFormatter(fmt1)

file2=logging.FileHandler('log2.log','a')
fmt2=logging.Formatter()
file2.setFormatter(fmt2)

logger=logging.Logger('s1',level=logging.ERROR)
logger.addHandler(file1)
logger.addHandler(file2)
logger.critical('test critical')

file2_1=logging.FileHandler('log2_1.log','a')
file2_1.setFormatter(fmt2)

logger2=logging.Logger('s2',level=logging.INFO)
logger2.addHandler(file2_1)
logger2.info('test info')