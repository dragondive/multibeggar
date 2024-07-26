from loguru import logger
import click

from multibeggar.multibeggar import Multibeggar
from sandbox import polars_learning


@click.command()
@click.option(
    "--transactions_file_path",
    type=click.Path(exists=True),
    required=True,
    help="Path to the excel file containing the transactions",
)
@click.option(
    "--complexity_tuning_factor",
    default=0.01,
    help="tuning factor for the multibeggar complexity algorithm",
    show_default=True,
)
@click.option(
    "--logfile",
    type=click.Path(),
    help="path to the logfile",
)
def entry_point(transactions_file_path, complexity_tuning_factor, logfile):
    if logfile:
        logger.add(logfile)

    logger.info("Hello World!")
    mb = Multibeggar(transactions_file_path=transactions_file_path, complexity_tuning_factor=complexity_tuning_factor)
    mb.beg()
    # polars_learning.read_transactions(transactions_file_path)


if __name__ == "__main__":
    entry_point()
