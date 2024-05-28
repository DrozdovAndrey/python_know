import logging

FORMAT = '{levelname}: {asctime}, module: {name}, function: {funcName}, line: {lineno},\nmsg: {msg}'

logging.basicConfig(filename='rectangle.log.', encoding='utf-8', level=logging.NOTSET, style='{', format=FORMAT)
logger = logging.getLogger('Rectangle')
