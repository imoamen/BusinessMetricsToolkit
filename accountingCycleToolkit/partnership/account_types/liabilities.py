import pandas as pd

from partnership.root_account import Account

class Liability(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_type(self):
        return 'debt'
       
    def balance(self):
        dr_sum = self.ledger['Debit'].sum()
        cr_sum = self.ledger['Credit'].sum()
        balance = cr_sum - dr_sum 
        return balance
    
    def show_ledger(self):
        balance_row = pd.DataFrame([['Balance:', '-', self.balance()]], columns=self.columns)
        return pd.concat([self.ledger, balance_row], ignore_index=True)

class AccountPayable(Liability):
    def account_type(self):
        return 'account_pay'

class NotesPayable(Liability):
    def account_type(self):
        return 'notes_pay'

class SalariesPayable(Liability):
    def account_type(self):
        return 'salaries_payable'
    
class UnearnedRevenue(Liability):
    def account_type(self):
        return 'unearned_revenue'

class ContraLiability(Account):
    def __init__(self, pr:int, name:str):
        super().__init__(pr, name)
    
    def account_type(self):
        return 'debt'
       
    def balance(self):                  
        dr_sum = self.ledger['Debit'].sum()
        cr_sum = self.ledger['Credit'].sum()
        balance = dr_sum - cr_sum 
        return balance
    
    def show_ledger(self):
        balance_row = pd.DataFrame([['Balance:', self.balance(), '-']], columns=self.columns)
        return pd.concat([self.ledger, balance_row], ignore_index=True)
