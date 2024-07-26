import polars
from loguru import logger

def read_transactions(filepath):
    # logger.debug(f"reading transactions from {filepath}.")
    # transactions_list = polars.read_excel(
    #     filepath
    # )
    # transactions_list = transactions_list.sort(by=["Name", "Date"])
    # with polars.Config() as polars_config:
    #     polars_config.set_tbl_rows(10000)
    #     logger.debug(transactions_list)
    df = polars.DataFrame(
        {
            "a": [1, 2, 3, 4],
            "b": [0.5, 4, 10, 13],
            "c": [True, True, False, True],
        }
    )

    print(
        df.with_columns(
            (polars.col(
                "a"
            ) * 2).alias("Hl e")
        )
    )