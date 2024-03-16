from loguru import logger
from loguru._handler import RotatingFile

handler = RotatingFile("file.log", max_size="1 MB", backup_count=3)
logger.add(handler)

logger.info("This message will be logged to a rotating file")


