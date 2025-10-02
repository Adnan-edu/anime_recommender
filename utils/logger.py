import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR,exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure the root logger to write logs to a file with a specific format and INFO level
logging.basicConfig(
    filename=LOG_FILE,  # Set the log file path
    format='%(asctime)s - %(levelname)s - %(message)s',  # Set the log message format
    level=logging.INFO  # Set the logging level to INFO
)

def get_logger(name):
    # Create or retrieve a logger with the specified name
    logger = logging.getLogger(name)
    # Set the logger's level to INFO (so it handles INFO and above)
    logger.setLevel(logging.INFO)
    # Return the configured logger instance
    return logger