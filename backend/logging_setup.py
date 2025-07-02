import logging
from logging import DEBUG
def logging_set(name,filename='server.log',level=DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:  # Prevent duplicate handlers
        file_handler = logging.FileHandler(filename)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.propagate = False  # Prevent interference from uvicorn loggers
    return logger
