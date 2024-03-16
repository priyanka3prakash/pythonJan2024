import logging
import logging.config
import os


# logging.config.fileConfig("11_logging.conf")

current_dir_name = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(current_dir_name, "11_logging.conf")


logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")
print()



# --- creata logger object
# create logger
logger = logging.getLogger("simpleExample")

# 'application' code
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
print()

# create logger
logger = logging.getLogger("GudoVan")

# 'application' code
logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")