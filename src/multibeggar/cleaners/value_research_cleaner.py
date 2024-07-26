import polars

class ValueResearchCleaner:
    def __init__(self):
        self.replace_pairs = ("Dir-G", "Direct Plan Growth"),

    def clean(self, transactions_list: polars.DataFrame):
        transactions_list = transactions_list.with_columns(
            polars.col("Name").str.replace_many(
                [pair[0] for pair in self.replace_pairs],
                [pair[1] for pair in self.replace_pairs]
            )
        )

        return transactions_list
