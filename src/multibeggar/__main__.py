from loguru import logger
import click

from multibeggar.multibeggar import Multibeggar


@click.command()
@click.option(
    "--complexity_tuning_factor",
    default=0.01,
    help="tuning factor for the multibeggar complexity algorithm",
    show_default=True,
)
def entry_point(complexity_tuning_factor):
    logger.info("Hello World!")
    mb = Multibeggar(complexity_tuning_factor=complexity_tuning_factor)


if __name__ == "__main__":
    entry_point()
