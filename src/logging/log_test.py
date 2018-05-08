# -*- coding: utf-8 -*-

import logging
"""
filename  Specifies that a FileHandler be created, using the specified
          filename, rather than a StreamHandler.
filemode  Specifies the mode to open the file, if filename is specified
          (if filemode is unspecified, it defaults to 'a').
format    Use the specified format string for the handler.
datefmt   Use the specified date/time format.
level     Set the root logger level to the specified level.
stream    Use the specified stream to initialize the StreamHandler. Note
          that this argument is incompatible with 'filename' - if both
          are present, 'stream' is ignored.
"""

def log_tt():
    logging.basicConfig(filename = "log.log",
                        format = "%(asctime)s - %(levelname)s - %(module)s: %(message)s",
                        datefmt = "%Y-%m-%d %H:%M:%S %p",
                        level = logging.DEBUG)

    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    
    logging.debug("==============")
    
    try:
        logging.info('into try')
        raise Exception('try error')
    except Exception as er:
        logging.warn('out try')


def multi_log_tt():
    error_log = logging.FileHandler("error.log", "a")
    error_fmt = logging.Formatter(fmt = "%(asctime)s - %(levelname)s - %(module)s: %(message)s")
    error_log.setFormatter(error_fmt)

    debug_log = logging.FileHandler("debug.log", "a")
    debug_fmt = logging.Formatter(fmt = "%(asctime)s - %(levelname)s: %(message)s")
    debug_log.setFormatter(debug_fmt)

    # 定义日志
    logger = logging.Logger("s1", level = logging.ERROR)
    logger.addHandler(error_log)
    logger.addHandler(debug_log)

    logger.error("error_log error")
    

if __name__ == "__main__":
    log_tt()
#     multi_log_tt()
