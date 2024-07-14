from Root import Account
import pandas as pd

class Revenue(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_type(self):
        return 'revenue'
        
    def balance(self):
        dr_sum = self.ledger['Debit'].sum()
        cr_sum = self.ledger['Credit'].sum()
        balance = cr_sum - dr_sum 
        return balance
    
    def show_ledger(self):
        balance_row = pd.DataFrame([['Balance:', '-', self.balance()]], columns=self.columns)
        return pd.concat([self.ledger, balance_row], ignore_index=True)

class ContraRev(Revenue):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def balance(self):
        dr_sum = self.ledger['Debit'].sum()
        cr_sum = self.ledger['Credit'].sum()
        balance = dr_sum - cr_sum
        return balance
    
    def show_ledger(self):
        balance_row = pd.DataFrame([['Balance:', self.balance(), '-']], columns=self.columns)
        return pd.concat([self.ledger, balance_row], ignore_index=True)