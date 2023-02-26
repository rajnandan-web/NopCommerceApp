import logging


class LogGeneration:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        handler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s", datefmt='%m/%d/%Y %I:%M:%S %p')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
