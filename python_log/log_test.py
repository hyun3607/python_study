import log

logger = log.get_logger("test")

def test_info():
    logger.info("info level")
    
def test_debug():
    logger.debug("debug level")

test_info()
test_debug()