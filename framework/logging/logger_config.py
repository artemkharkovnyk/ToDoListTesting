import logging


tests_logger = logging.getLogger("tests_logger")
tests_logger.setLevel(logging.INFO)
tests_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
tests_file_handler = logging.FileHandler("tests.log")
tests_file_handler.setFormatter(tests_formatter)
tests_logger.addHandler(tests_file_handler)
