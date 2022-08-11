import logging

def get_logger(name=None):
    logger = logging.getLogger(name)

    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - [%(funcName)s:%(lineno)d] - %(message)s")
    
    console = logging.StreamHandler()
    file_handler_debug = logging.FileHandler(filename="log_debug.log")
    file_handler_info = logging.FileHandler(filename="log_info.log")

    console.setLevel(logging.INFO)
    file_handler_debug.setLevel(logging.DEBUG)
    file_handler_info.setLevel(logging.INFO)

    console.setFormatter(formatter)
    file_handler_debug.setFormatter(formatter)
    file_handler_info.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler_debug)
    logger.addHandler(file_handler_info)
	
    return logger