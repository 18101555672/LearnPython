import logging
# 简单使用
logging.debug('DEBUG')
logging.info('INFO')
logging.warning('WARNING')
logging.error('ERROR')
logging.critical('CRITICAL')
#  WARNING :     roo      : WARNING
# 日志级别  logger实例名称  日志消息内容
# 默认日志级别为WARNING（即只有日志级别等于或高于WARNING的日志信息才会输出）

# 日志级别
# 级别      何时使用
# DEBUG     详细信息，典型地调试问题时会感兴趣
# INFO      证明事情按预期工作
# WARNING   表明发生了一些意外，或者不久的将来会发生问题，但是软件还是在正常工作
# ERROR     由于更严重的问题，软件已经不能执行一些功能了
# CRITICAL  严重错误，表明软件已经不能继续运行了

# 简单配置
# logging.basicConfig(filename='logger.log',level=logging.DEBUG)
# Logger记录器，暴露了应用程序代码能直接使用的接口
# Handler处理器，将记录器产生的日志记录发送至合适的目的地
# Filter过滤器，提供了更好的粒度控制，可以决定输出哪些日志记录
# Formatter格式化器，指明了最终输出中日志记录的布局

# logger记录器
# 创建
logger = logging.getLogger('log')
# 设置日志级别
logger.setLevel(logging.DEBUG)
# 增加处理器
logger.addHandler('handlerName')
# 删除处理器
logger.removeHandler('handlerName')

# Handler处理器
# 三种常用的Handler处理器：StreamHandler,FileHandler,NullHandler
# 创建StreamHandler
sh = logging.StreamHandler(stream=None)
# 创建FileHandler
fh = logging.FileHandler('fileHandlerName',mode='a',encoding=None,delay=False)
# 指定日志界别
sh.setLevel('DEBUG')
# 设置一个格式化器
sh.setFormatter('formatterName')
# 增加过滤器，最多一个
sh.addFilter('filterName')
# 删除过滤器
sh.removeFilter('filterName')

# Formatter格式化器
# 创建
formatter = logging.Formatter(fmt=None,datefmt=None)
# fmt是消息的格式化字符串，如果不指明，则使用'%(message)s'
# datefmt是日期的格式化字符串，如果不指明，则使用ISO8601日期格式
# 默认的时间格式为%Y-%m-%d %H:%M:%S

# Filter过滤器
# 创建
filter = logging.Filter(name='filterName')
# Handlers和Loggers可以使用Filters来完成比级别更复杂的过滤
# Filter基类只允许特定Logger层次以下的事件
# 例如用'A.B'初始化的Filter允许Logger'A.B','A.B.C','A.B.C.D','A.B.D'等记录的事件，logger'A.BB','B.A.B'等就不行
# 如果用空字符串来初始化，所有的事件都接受

# 相关概念总结：
# Logger是一个树形层级结构
# Logger可以包含一个或多个Handler和Filter，即Logger与Handler或Fitler是一对多的关系
# 一个Logger实例可以新增多个Handler，一个Handler可以新增多个格式化器或多个过滤器，而且日志级别将会继承

# 配置方式
# basciConfig()通过简单方式配置
# fileConfig()通过配置文件配置
# dictConfig()通过简配置字典配置
# listen()通过网络配置

# basicConfig关键字参数
# 关键字    描述
# filename  创建一个FileHandler，使用指明的文件名，而不是使用StreamHandler
# filemode  如果指明了文件名，指明打开文件的模式，默认为'a'
# format    Handler使用指明的格式化字符串
# datefmt   使用指明的日期时间格式
# level     指明根logger的级别
# stream    使用指明的流来初始化StreamHandler，该参数与filename不兼容，如果两者都有，则忽略tream、

# format格式
# 格式            描述
# %(levelno)s       打印日志级别的数值
# %(levelname)s     打印日志级别名称
# %(pathname)s      打印当前执行程序的路径
# %(filename)s      打印当前执行程序的名称
# %(funcName)s      打印当前执行函数的名称
# %(lineno)d        打印日志的当前行号
# %(asctime)s       打印日志的时间
# %(thread)d        打印线程ID
# %(threadName)s    打印线程名称
# %(process)d       打印进程ID
# %(message)s       打印日志信息

# datefmt格式
# 参考MOOC_Python/week_03/python_02.py