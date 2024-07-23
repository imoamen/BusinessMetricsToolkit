import pandas as pd

import partnership.root_account as root

class IncomeStatement:
    
    exp_acc = {
        'ttl_cogs':0, 'ttl_salaries':0, 'ttl_rent':0, 
        'ttl_utilities':0, 'ttl_interest':0, 'ttl_insurance':0, 'ttl_depreciation':0, 
        'ttl_depletion':0, 'ttl_bad_debt':0, 'ttl_loss_disposal':0, 
        'ttl_othr_exp':0, 'ttl_exp':0 
        }
    rev_acc = {
        'ttl_sales':0, 
        'ttl_othr_contra_revenue':0, 'ttl_gain_disposal':0, 'ttl_discount':0, 'ttl_returns_allowances':0, 
        'ttl_othr_rev':0, 'ttl_rev':0
        }

    def expense_prep(self, used_account:root.Account):

        if used_account.account_sub_type() == 'cogs':
            self.exp_acc['ttl_cogs'] +=used_account.balance()
            self.exp_acc['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'salaries':
            self.exp_acc['ttl_salaries'] +=used_account.balance()
            self.exp_acc['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'rent':
            self.exp_acc['ttl_rent'] +=used_account.balance()
            self.exp_acc['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'utilities':
            self.exp_acc['ttl_utilities'] +=used_account.balance()
            self.exp_acc['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'interest':
            self.exp_acc['ttl_interest'] +=used_account.balance()
            self.exp_acc['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'insurance':
            self.exp_acc['ttl_insurance'] +=used_account.balance()
            self.exp_acc['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'depreciation':
            self.exp_acc['ttl_depreciation'] +=used_account.balance()
            self.exp_acc['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'depletion':
            self.exp_acc['ttl_depletion'] +=used_account.balance()
            self.exp_acc['ttl_exp'] +=used_account.balance()

        elif used_account.account_sub_type() == 'bad_debt':
            self.exp_acc['ttl_bad_debt'] +=used_account.balance()
            self.exp_acc['ttl_exp'] +=used_account.balance()
        
        elif used_account.account_sub_type() == 'loss_disposal':
            self.exp_acc['ttl_loss_disposal'] +=used_account.balance()
            self.exp_acc['ttl_exp'] +=used_account.balance()

        else:
            if used_account.account_type() == 'expense':
                self.exp_acc['ttl_othr_exp'] +=used_account.balance()
                self.exp_acc['ttl_exp'] +=used_account.balance()
            else:
                print(f'An error occured while incrementing the expense account:`{used_account.name}`')
        

    def revenue_prep(self, used_account:root.Account):
        
        if used_account.account_sub_type() == 'sales':
            self.rev_acc['ttl_sales'] +=used_account.balance()
            self.rev_acc['ttl_rev'] +=used_account.balance()

        elif used_account.account_sub_type() == 'gain_disposal':
            self.rev_acc['ttl_gain_disposal'] +=used_account.balance()
            self.rev_acc['ttl_rev'] +=used_account.balance()

        elif used_account.account_sub_type() == 'discount':
            self.rev_acc['ttl_discount'] +=used_account.balance()
            self.rev_acc['ttl_rev'] -=used_account.balance()

        elif used_account.account_sub_type() == 'returns_allowances':
            self.rev_acc['ttl_returns_allowances'] +=used_account.balance()
            self.rev_acc['ttl_rev'] -=used_account.balance()
        
        else:
            if used_account.account_type() == 'revenue':
                self.rev_acc['ttl_othr_rev'] +=used_account.balance()
                self.rev_acc['ttl_rev'] +=used_account.balance()
            
            elif used_account.account_type() == 'contra_revenue':
                self.rev_acc['ttl_othr_contra_revenue'] +=used_account.balance()
                self.rev_acc['ttl_rev'] -=used_account.balance()
            
            else:   
                print(f'An error occured while incrementing the revenue account:`{used_account.name}`')

        
    def income_data(self, in_acc:list):
        
        for used_account in in_acc:
            try:
                if used_account.account_type() not in ['revenue', 'contra_revenue', 'expense']:
                    
                    print(f"""
                        Account:`{used_account.name}` is an Asset or Liability account,\n 
                        make sure only instances of the following classes or there subclasses are entered:\n
                        'Revenue', 'Expense'
                        """) 
                
                elif used_account.account_type() in [
                    'revenue', 'contra_revenue'
                    ]:
                    self.revenue_prep(used_account)
                
                elif used_account.account_type() == 'expense':
                    self.expense_prep(used_account)
            except (ValueError, TypeError, NameError):
                print('Fault, contact admin')

        exp_acc_keys = ['ttl_cogs', 'ttl_salaries', 'ttl_rent', 'ttl_utilities', 'ttl_interest', 'ttl_insurance', 'ttl_depreciation', 
                        'ttl_depletion', 'ttl_bad_debt', 'ttl_loss_disposal', 'ttl_othr_exp']
        used_exp_acc = self.exp_acc
        for acc in exp_acc_keys:
            if 0 == self.rev_acc[acc]:
                used_exp_acc.pop(acc)
        
        rev_acc_keys = ['ttl_sales', 'ttl_othr_contra_revenue', 'ttl_gain_disposal', 'ttl_discount', 'ttl_returns_allowances', 'ttl_othr_rev']
        used_rev_acc = self.rev_acc
        for acc in rev_acc_keys:
            if 0 == self.rev_acc[acc]:
                used_rev_acc.pop(acc)
        
        income_dict = used_exp_acc.update(used_rev_acc)
        income_dict.update({'net_income': income_dict['ttl_rev'] - income_dict['ttl_exp']})
        pd.DataFrame(list(income_dict.items()), columns=['Account Name', 'Amount'])
  
        



