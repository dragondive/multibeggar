import polars
import requests

class GeneralDataProvider:
    # todo: rename to specific data provider, so we can use
    # other data providers or a combination later.
    def __init__(self):
        pass

    def update_investment_data(self, transactions_list: polars.DataFrame):
        transactions_list = transactions_list.with_columns(
            polars.struct(["Type", "Name"])
            .map_elements(lambda x: self._get_symbol(x))
            .alias("Symbol")
        )

        # transactions_list = transactions_list.map_rows(lambda x: self._get_symbol(x))
        # transactions_list = transactions_list.with_columns(
        #     transactions_list.apply(self._get_symbol)
        # )
        # # transactions_list = transactions_list.with_columns(transactions_list.select(
        # #     polars.struct(["Name", "Type"]).apply(self._get_symbol)
        # # ))
        # transactions_list = transactions_list.with_columns(
        #     [
        #         transactions_list.select(polars.struct(["Name", "Type"]))
        #         # (polars.col("Type").alias("Symbol"))
        #     ]
        # )
        # # transactions_list.with_columns(
        # #     (self._get_symbol(polars.col("Type"))).alias("Symbol")
        # # )
        # # # print(
        # #     transactions_list.with_columns(polars
        # #     .when(polars.col("Type") == "Mutual Fund")
        # #         .then(polars.col("Name").apply(self._get_mf_symbol))
        # #     .when(polars.col("Type") == "Stock")
        # #         .then(polars.col("Name").apply(self._get_stock_symbol))
        # #     .alias("Symbol")
        # #     )
        # # )
        print(transactions_list)

    def _get_symbol(self, transaction: dict) -> str:
        # print(transaction)
        if transaction["Type"] == "Mutual Fund":
            return self._get_mf_symbol(transaction["Name"])
        elif transaction["Type"] == "Stock":
            return self._get_stock_symbol(transaction["Name"])
        else:
            return None

    def _get_mf_symbol(self, name: str) -> str:
        response = requests.get(f"https://api.mfapi.in/mf/search?q={name.replace(' ', '%20')}")
        data = response.json()

        if len(data) == 1:
            return str(data[0]['schemeCode'])
        elif len(data) > 1:
            # The response sometimes has identical entries with some formatting difference
            # in the scheme name, so we do this workaround to eliminate such "duplicates"
            unique_data = []
            seen_scheme_codes = set()
            for item in data:
                if item['schemeCode'] not in seen_scheme_codes:
                    unique_data.append(item)
                    seen_scheme_codes.add(item['schemeCode'])
            
            if len(unique_data) == 1:
                return str(unique_data[0]['schemeCode'])
            else:
                return None # todo raise exception
        else:
            return None # todo raise exception
        
    
    def _get_stock_symbol(self, name: str) -> str:
        return "Y"
