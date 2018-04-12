import logging
# 显示配置
# 创建logger
logger_name = 'example'
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

# 创建fileHandler
log_path = './log.log'
fh = logging.FileHandler(log_path)
fh.setLevel(logging.WARNING)

# 创建formatter
fmt = '%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s'
datefmt = '%Y-%m-%d %a %H:%M:%S'
formatter = logging.Formatter(fmt=fmt,datefmt=datefmt)

# 向logger添加Handler和formatter
fh.setFormatter(formatter)
logger.addHandler(fh)

# 打印日志
logger.debug('DEBUG')
logger.info('INFO')
logger.warning('WARNING')
logger.error('ERROR')
logger.critical('CRITICAL')