import Root as root
import pandas as pd
class Journaling:
    general_journal = pd.DataFrame(columns=['date', 'account_name', 'pr', 'dr', 'cr'])

    def two_line_journal_entry(self, date:str, dr_acc:root.Account, cr_acc:root.Account, amount:float):

        dr_acc.transaction(date, amount)
        cr_acc.transaction(date, 0 ,amount)

    
        dr_entry = pd.DataFrame([[date, dr_acc.name, dr_acc.pr, amount, 0]]
                        , columns=['date', 'account_name', 'pr', 'dr', 'cr'])
        
        cr_entry = pd.DataFrame([[date, cr_acc.name, cr_acc.pr, 0, amount]]
                        , columns=['date', 'account_name', 'pr', 'dr', 'cr'])
        
        entry = pd.concat([dr_entry, cr_entry], ignore_index=True)

        self.general_journal = pd.concat([self.general_journal, entry], ignore_index=True)

    

