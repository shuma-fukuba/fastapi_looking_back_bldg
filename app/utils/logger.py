import logging
import os
import yaml
import env
from logging import config


def get_logger(name: str = '', log_dir: str = '/var/log/app'):
    base = os.path.dirname(os.path.abspath(__file__))
    conf_file = os.path.join(base, 'logger.yml')

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        logfile = f'{log_dir}/app.log'
        open(logfile, 'w')

    with open(conf_file, 'r') as f:
        config.dictConfig(yaml.safe_load(f))

    logger = logging.getLogger(name)

    log_level = logging.INFO
    if env.APP_ENV == 'development':
        log_level = logging.DEBUG

    logger.setLevel(log_level)

    return logger
