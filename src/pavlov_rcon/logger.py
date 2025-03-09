from loguru import logger 

logger.add("rcon.log", rotation="1 week", level="INFO", format="{time} {level} {message}") 

logger.info("Logger initialized")