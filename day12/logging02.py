import logging
from logging.handlers import HTTPHandler
import sys
logger01 = logging.getLogger(__name__)
logger01.setLevel(level=logging.DEBUG)

# StreamHandler控制台输出
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
logger01.addHandler(stream_handler)

# FileHandler打印到output.log文件中
file_handler = logging.FileHandler('output.log')
file_handler.setLevel(level=logging.WARN)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(lineno)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger01.addHandler(file_handler)

# log
logger01.info('This is a log info')
logger01.debug('Debugging')
logger01.warning('Warning exists')
logger01.info('Finish')