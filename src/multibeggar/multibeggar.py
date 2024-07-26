from loguru import logger
import os
import polars
from multibeggar.cleaners.value_research_cleaner import ValueResearchCleaner
from multibeggar.data_providers.general_data_provider import GeneralDataProvider

class Multibeggar:
    def __init__(self, transactions_file_path: str | os.PathLike , complexity_tuning_factor: float):
        self.complexity_tuning_factor = complexity_tuning_factor
        self.transactions_file_path = transactions_file_path

        self.transactions_list = None
                ## todo: configure cleaner class
        self.cleaner = ValueResearchCleaner()
        self.data_provider = GeneralDataProvider()
        # todo: configure cleaner dynamically so can be used with other data sources
        # left as an exercise to the reader ... or whatever. 
    
    def beg(self):
        logger.info(f"Reading transactions list from {self.transactions_file_path}")
        self.transactions_list = polars.read_excel(self.transactions_file_path)
        logger.debug(type(self.transactions_list))

        # todo: cleanup names
        self.transactions_list = self.cleaner.clean(self.transactions_list)
        self.transactions_list = self.data_provider.update_investment_data(self.transactions_list)
        self._log_transactions_list()

        # self.transactions_list = self.transactions_list.sort(by=["Type", "Name", "Date"])
        # # self._log_transactions_list(prefix_message="sorted")
        
        # self.__compute_daywise_portfolio()
        


    def _log_transactions_list(self, number_of_rows: int = 10000, prefix_message: str = ""):
        with polars.Config() as polars_config:
            polars_config.set_tbl_rows(number_of_rows)
            logger.debug(f"{prefix_message} {self.transactions_list=}")

    def __compute_daywise_portfolio(self):
        # ongoing_date = None
        # daily_portfolio = polars.DataFrame(schema=self.transactions_list.schema)


        ## todo: configure data provider class

        # todo: get symbols for the name
        # todo: get bonus, split, rights data
        # todo: adjust transactions_list with above


        x = self.transactions_list.with_columns(
            polars.col("Units").cum_sum().over("Name")
        ).sort(by="Date")

        # print(self.transactions_list.group_by(["Date", "Name"], maintain_order=True).count)
        with polars.Config() as polars_config:
            polars_config.set_tbl_rows(100)
            # print(self.transactions_list.with_columns(polars.col("Units").cum_sum().over(["Name"])))
            # print(x)

        # with polars.Config() as polars_config:
        #     polars_config.set_tbl_rows(1000)
        #     logger.debug(f"{grouped=}")

        # print(self.transactions_list.select(polars.cum_sum("Units")))
        # for row in self.transactions_list.iter_rows():
        #     print(row)
        #     # date = row["Date"]
        #     # self.logger.debug(f"{date=}")