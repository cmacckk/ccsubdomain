import logging
import colorlog
# from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s: %(message)s%(reset)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red'
    },
    reset=True,
    style='%'
)

# add console handler, output log to console
console_handler = logging.StreamHandler()

# add log file handler, output log to log file, 2MB, 2 backup file
# file_handler = RotatingFileHandler('./log/subdomain_info.log', encoding='utf-8', maxBytes=2048, backupCount=2)

# add handler to logger
logger.addHandler(console_handler)
# logger.addHandler(file_handler)

# setting formatter and give handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# formatter give handler
console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)
