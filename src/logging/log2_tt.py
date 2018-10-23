# -*- coding: utf-8 -*-
'''
Created on 2018年7月3日

@author: Hong
'''

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

LOG = logging.getLogger()

def log_tt():
    
    logging.basicConfig(
#         filename="log.log",
        format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d %(module)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
    )

    LOG.debug("debug")
    LOG.info("info")
    LOG.warning("warning")
    LOG.error("error")
    
    LOG.debug("==============")
    
    try:
        LOG.info('into try')
        raise Exception('try error')
    except Exception as er:
        LOG.warn('out try')

if __name__ == "__main__":
    log_tt()
