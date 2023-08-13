from loguru import logger

class Multibeggar:
    def __init__(self, complexity_tuning_factor: float):
        logger.debug("Multibeggar created!")
        self.complexity_tuning_factor = complexity_tuning_factor
