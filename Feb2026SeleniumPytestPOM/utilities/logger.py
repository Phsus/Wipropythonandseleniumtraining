import logging
import os


def get_logger():
    # 1. Create a custom logger using the module name
    logger = logging.getLogger(__name__)

    # 2. Prevent duplicate log entries if the function is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.INFO)

    # 3. Create a 'Logs' folder in the root directory
    # This logic finds the parent directory of 'utilities' to place the folder at the root
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Logs")
    os.makedirs(log_dir, exist_ok=True)


    log_file_path = os.path.join(log_dir, "automation.log")


    file_handler = logging.FileHandler(log_file_path)


    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)


    logger.addHandler(file_handler)

    return logger