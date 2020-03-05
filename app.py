# 存放全局变量,公有的配置函数活着了类
import logging
import os
from logging import  handlers

# 定义文件的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 定义全局变量HEADERS和EMPID和DEPIP
HEADERS = {"Content-Type":"application/json"}
EMPID = None
DEPID = None


# 日志
def init_log():
    #1.定义一个初始化日志配置的函数,初始化日志的输出路径
    #2.创建日志器
    logger = logging.getLogger()
    #3.设置日志等级
    logger.setLevel(logging.INFO)
    #4.创建处理器,通过处理控制日志的打印
    sh = logging.StreamHandler()
    fh = logging.handlers.TimedRotatingFileHandler(BASE_DIR+"/log/IHRM.log",
                                                   when='S',interval=10,
                                                   backupCount=3,encoding='utf-8')
    #5.设置日志的格式,所以需要创建格式和格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt)
    #6将格式器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    #7.将处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)


if __name__ == '__main__':
    init_log()
    logging.info("test test")