import logging
# logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')#配置
# logger = logging.getLogger(__name__)
#
# logger.info('This is a log info')
# logger.debug('Debugging')
# logger.warning('Warning exists')
# logger.info('Finish')
# logger.error('Error')

#2021/01/17 11:09:31 - __main__ - INFO - This is a log info
logging.basicConfig(level=logging.DEBUG,filename='output.log',datefmt='%Y/%m/%d %H:%M:%S',format='%(asctime)s - %(name)s - %(lineno)s - %(levelname)s - %(message)s')
logger2 = logging.getLogger(__name__)
logger2.info('This is a log info')
logger2.debug('Debugging')
logger2.warning('Warning exists')
logger2.info('Finish')
logger2.error('Error')


