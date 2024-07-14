import pandas as pd

class Account:
    def __init__(self, pr:int, name: str):
        self.pr = pr
        self.name = name
    columns = ['Date', 'Debit', 'Credit']
    ledger = pd.DataFrame(columns=columns)

    def transaction(self, date: str, dr_amount:float = 0, cr_amount:float = 0):
        transaction = pd.DataFrame([[date, dr_amount, cr_amount]], columns=self.columns)
        self.ledger = pd.concat([self.ledger, transaction], ignore_index=True)
                