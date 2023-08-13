from loguru import logger
from multibeggar.multibeggar import Multibeggar


def entry_point():
    logger.info("Hello World!")
    mb = Multibeggar(complexity_tuning_factor=0.42)


if __name__ == "__main__":
    entry_point()
