import logging

logging.basicConfig(filename='log.log', \
                    format='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s', \
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=logging.NOTSET)
logging.critical('critical')
logging.error('error')
logging.warning('warnning')
logging.info('info')
logging.debug('debug')
logging.log(logging.INFO,'NOTSET')
