import pandas as pd
# Creating main company
class Company:
    def __init__(
            self, date_record, cash = 0, account_receivables = 0, inventory = 0, current_assets = 0
            , noncurrent_assets = 0, accu_depr = 0
            , intangible_assets = 0, longterm_investments = 0
            , current_lia = 0, noncurrent_lia = 0
            , owners_equity = 0, net_income = 0, ebit = 0
            , total_rev = 0, sales_rev  = 0, total_exp = 0, operating_exp = 0, interest_exp = 0, depr_exp = 0, wages_exp = 0
            ):
        
        # Assigning values to attributes
        # balance sheet date
        self.date_record = date_record
        # Current Assets
        self.cash = cash
        self.account_receivables = account_receivables
        self.inventory = inventory
        self.current_assets = current_assets
        
        # Non-current assets and deperciatables
        self.noncurrent_assets = noncurrent_assets
        self.accu_depr = accu_depr
        self.intangible_assets = intangible_assets
        self.longterm_investments = longterm_investments
        
        # Liabilties
        self.current_lia = current_lia
        self.noncurrent_lia = noncurrent_lia
        
        # Equity
        self.owners_equity = owners_equity
        self.net_income = net_income 
        self.ebit = ebit        
        
        # Income statement 
        self.total_rev = total_rev
        self.sales_rev = sales_rev
        self.total_exp = total_exp
        self.operating_exp = operating_exp
        self.interest_exp = interest_exp
        self.depr_exp = depr_exp
        self.wages_exp = wages_exp
    
    # Totals Methods
    # - Total assets calculation
    def total_assets(self):
            return self.cash + self.account_receivables + self.inventory +self.noncurrent_assets + self.current_assets + self.intangible_assets + self.longterm_investments - self.accu_depr
        
    # - Total liabilities calculation
    def total_lia(self):  
        return self.current_lia + self.noncurrent_lia

    # Financial Ratios methods
    # all methods return method that are inhreited by subclasses
    # add validation test to makes sure no division by zero
    # - Liquidity ratio calculation
    # -- Current Ratio
    def current_ratio(self):
        try:
            return self.current_assets / self.current_lia
        except ZeroDivisionError:
            return 0

    # -- Quick ratio
    def quick_ratio(self):
        try:
            return (self.current_assets - self.inventory) / self.current_lia
        except ZeroDivisionError:
            return 0

    # --Cash ratio
    def cash_ratio(self):
        try:
            return self.cash / self.current_lia
        except ZeroDivisionError:
            return 0

    # - Financial leverage
    # -- Total dept ratio
    def total_debt_ratio(self):
        try:
            return (self.total_assets() - self.owners_equity) / self.total_assets() 
        except ZeroDivisionError:
            return 0

    # -- Dept Equity ratio
    def dept_equity_ratio(self):
        try:
            return self.total_lia() / self.owners_equity
        except ZeroDivisionError:
            return 0

    # -- Equity Multiplier
    def equity_multi(self):
        try:
            return self.total_assets() / self.owners_equity
        except ZeroDivisionError:
            return 0

    # -- Times interest earned ratio
    def tie(self):
        try:
            return self.ebit / self.interest_exp
        except ZeroDivisionError:
            return 0

    # -- Cash Coverage Ratios
    def cash_cov_ratio(self):
        try:
            return (self.ebit + self.depr_exp) / self.interest_exp
        except ZeroDivisionError:
            return 0

    # - Turnover Measures
    # -- Receivables turnover
    def rece_trnovr(self):
        try:
            return self.sales_rev / self.account_receivables
        except ZeroDivisionError:
            return 0

    # -- Days’ sales in receivables
    def days_sales_rece_trnover(self):
        try:
            return 365 / self.rece_trnovr()
        except ZeroDivisionError:
            return 0

    #  -- Total asset turnover
    def total_asset_trnovr(self):
        try:
            return self.sales_rev / self.total_assets()
        except ZeroDivisionError:
            return 0

    # - Profitability Measures
    # -- Profit margin
    def profit_marg(self):
        try:
            return self.net_income / self.total_rev
        except ZeroDivisionError:
            return 0

    # -- Return on assets
    def return_assets(self):
        try:
            return self.net_income / self.total_assets()
        except ZeroDivisionError:
            return 0

    # -- Return on equity
    def return_equity(self):
        try:
            return self.net_income / self.owners_equity
        except ZeroDivisionError:
            return 0

    def wages_rev_ratio(self):
        try:
            return self.wages_exp / self.total_rev
        except ZeroDivisionError:
            return 0

#Hotel subclass
class Hotel(Company):
    def __init__(
        self, date_record, room_num_aval, room_rev = 0, room_num_occ = 0, room_num_sold = 0, 
        cash = 0, account_receivables = 0, inventory = 0, current_assets = 0, 
        noncurrent_assets = 0, accu_depr  = 0, 
        intangible_assets = 0, longterm_investments = 0, 
        current_lia = 0, noncurrent_lia = 0, 
        owners_equity = 0, net_income = 0, ebit = 0, 
        total_rev = 0, sales_rev = 0, total_exp = 0, operating_exp = 0, interest_exp = 0, depr_exp = 0, wages_exp = 0  
        ):
        
        # Intializing subclass attributes
        self.room_num_aval = room_num_aval
        self.room_num_occ = room_num_occ
        self.room_rev = room_rev
        self.room_num_sold = room_num_sold

        # initialize attributes from the base class within the subclasses
        super().__init__(
        date_record
        , cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp 
        )
        
    # Other metrics methods
    # - gross operation profit calculation 
    def GOP(self):
        try:    
            return self.total_rev - self.operating_exp
        except ZeroDivisionError:
            return 0

    # - Occupation rate
    def occ_rate(self):
        try:    
            return self.room_num_occ / self.room_num_aval
        except ZeroDivisionError:
            return 0

    # Specific Financial Ratios methods
    # - Average daily rate
    def ave_daily_rate(self):
        try:    
            return self.room_rev / self.room_num_occ
        except ZeroDivisionError:
            return 0

    # - Revenue per available rooms
    def rev_per_room_aval(self):
        try:    
            return self.room_rev / self.room_num_aval
        except ZeroDivisionError:
            return 0

    # - Gross Operating Profit per Available Room
    def GOPPAR(self):
        try:    
            return self.GOP() / self.room_num_aval
        except ZeroDivisionError:
            return 0

    # - Revenue Per Available Rooms
    def rev_par(self):
        try:    
            return self.ave_daily_rate() * self.occ_rate()
        except ZeroDivisionError:
            return 0

    # Initiate a dataframe for instance, to be used for 
    def create_df(self):
        # Gathering data in single list
        list_ratios = [
            self.date_record,
            self.GOPPAR(), self.rev_per_room_aval(), self.rev_par(), # specific methods
            # default methods
            self.current_ratio(), self.quick_ratio(), self.cash_ratio(), # liquidity ratios
            self.total_debt_ratio(), self.dept_equity_ratio(), self.equity_multi(), self.tie(), self.cash_cov_ratio(), # financial leverage ratios
            self.rece_trnovr(), self.days_sales_rece_trnover(), self.total_asset_trnovr(), # turnover ratios 
            self.profit_marg(), self.return_assets(), self.return_equity(), self.wages_rev_ratio() # profitability ratios
        ]
        # Creating a list of column names
        columns = [
            'Period'
            , 'GOPPAR', 'Revenue per Available Room', 'Revenue Per Available Rooms' # hotel specific ratios
            , 'Current Ratio', 'Quick ratio', 'Cash Ratio' # liquidity ratios
            , 'Total Debt Ratio', 'Debt to Equity', 'Equity Multiplier', 'Times Interest Earned', 'Cash Coverage' # financial leverage ratios
            , 'Receivables Turnover', 'Days\' sales Receivables Turnover', 'Total Assets Turnover' # turnover ratios
            , 'Profit Margin', 'Return on Assets', 'Return on Equity', 'Payroll(wages) to Revenue' # profitability ratios
        ]  
        # Creating dataframe from values under respective columns
        df = pd.DataFrame([list_ratios], columns=columns)
        # Setting Period date as index
        df.set_index('Period', inplace=True)
        return df
    
# Trade companies subclass
class Trade(Company):
    def __init__(
        self, date_record, 
        cogs = 0, ave_inv = 0, 
        cash = 0, account_receivables = 0, inventory = 0, current_assets = 0, 
        noncurrent_assets  = 0, accu_depr = 0, 
        intangible_assets = 0, longterm_investments = 0, 
        current_lia = 0, noncurrent_lia = 0, 
        owners_equity = 0, net_income  = 0, ebit = 0, 
        total_rev = 0, sales_rev  = 0, total_exp = 0, operating_exp = 0, interest_exp = 0, depr_exp = 0, wages_exp = 0  
        ):
        
        # Intializing subclass attributes
        self.cogs = cogs
        self.ave_inv = ave_inv

        # initialize attributes from the base class within the subclasses
        super().__init__(
        date_record
        , cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        )

    # Specific Financial Ratios methods
    # Inventory turnover 
    def inv_trnovr(self):
        try:
            return self.cogs / self.ave_inv
        except ZeroDivisionError:
            return 0
    # Days’ sales in inventory 
    def days_sales_inv_trnovr(self):
        try:    
            try:
                return 365 / self.inv_trnovr()
            except ZeroDivisionError:
                return 0
        except ZeroDivisionError:
            return 0
        
    # Initiate a dataframe for instance, to be used for 
    def create_df(self):
        # Gathering data in single list
        list_ratios = [
                    self.date_record,
                    self.inv_trnovr(), self.days_sales_inv_trnovr() # special methods
                    # default methods
                    , self.current_ratio(), self.quick_ratio(), self.cash_ratio() # liquidity ratios
                    , self.total_debt_ratio(), self.dept_equity_ratio(), self.equity_multi(), self.tie(), self.cash_cov_ratio() # finacial leverage ratios
                    , self.rece_trnovr(), self.days_sales_rece_trnover(), self.total_asset_trnovr() # turnover ratios 
                    , self.profit_marg(), self.return_assets(), self.return_equity(), self.wages_rev_ratio() # profitability ratios        ]
        ]
        # Creating a list of column names
        columns = [
            'Period'
            , 'Inventory Turnover', 'Days\' sales inventory turnover'
            , 'Current Ratio', 'Quick ratio', 'Cash Ratio'
            , 'Total Debt Ratio', 'Debt to Equity', 'Equity Multiplier', 'Times Interest Earned', 'Cash Coverage'
            , 'Receivables Turnover', 'Days\' sales Receivables Turnover', 'Total Assets Turnover'
            , 'Profti Margin', 'Return on Assets', 'Return on Equity', 'Payroll(wages) to Revenue'
        ]  
        # Creating dataframe from values under respective columns
        df = pd.DataFrame([list_ratios], columns = columns)
        # Setting Period date as index
        df.set_index('Period', inplace=True)
        return df  
        
#Agriculture subclass
class Agriculture(Company):
    def __init__(
        self, date_record, 
        total_farm_area = 0, total_farm_rev = 0, total_num_stock = 0, total_stock_rev = 0,
        cash = 0, account_receivables = 0, inventory = 0, current_assets = 0, noncurrent_assets  = 0, accu_depr = 0, 
        longterm_investments = 0, 
        current_lia = 0, noncurrent_lia = 0, 
        owners_equity = 0, net_income  = 0, ebit = 0, 
        total_rev = 0, sales_rev = 0, total_exp = 0, operating_exp = 0, interest_exp = 0, depr_exp = 0, wages_exp = 0
        ):
        
        # Intializing subclass attributes
        self.total_farm_area = total_farm_area
        self.total_farm_rev = total_farm_rev
        self.total_num_stock = total_num_stock
        self.total_stock_rev = total_stock_rev

        # initialize attributes from the base class within the subclasses
        super().__init__(
        date_record
        , cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        )
        
    # Specific Financial Ratios methods
    # yield per unit of area
    def land_yield(self):
        try:    
            return self.total_farm_rev / self.total_farm_area
        except ZeroDivisionError:
            return 0
        
    # yield per livestock
    def livestock_yield(self):
        try:    
            return self.total_stock_rev / self.total_num_stock
        except ZeroDivisionError:
            return 0
        
    # initiate a dataframe for instance, to be used for 
    def create_df(self):
        # Gathering data in single list
        list_ratios = [
            self.date_record,
            self.land_yield(), self.livestock_yield(), # specific methods
            # default methods
            self.current_ratio(), self.quick_ratio(), self.cash_ratio(), # liquidity ratios
            self.total_debt_ratio(), self.dept_equity_ratio(), self.equity_multi(), self.tie(), self.cash_cov_ratio(), # financial leverage ratios
            self.rece_trnovr(), self.days_sales_rece_trnover(), self.total_asset_trnovr(), # turnover ratios 
            self.profit_marg(), self.return_assets(), self.return_equity(), self.wages_rev_ratio() # profitability ratios
        ]
        # Creating a list of column names
        columns = [
            'Period'
            , 'Land Yield', 'Livestock Yield' # agriculture specific ratios
            , 'Current Ratio', 'Quick ratio', 'Cash Ratio' # liquidity ratios
            , 'Total Debt Ratio', 'Debt to Equity', 'Equity Multiplier', 'Times Interest Earned', 'Cash Coverage' # financial leverage ratios
            , 'Receivables Turnover', 'Days\' sales Receivables Turnover', 'Total Assets Turnover' # turnover ratios
            , 'Profit Margin', 'Return on Assets', 'Return on Equity', 'Payroll(wages) to Revenue' # profitability ratios
        ]  
        # Creating dataframe from values under respective columns
        df = pd.DataFrame([list_ratios], columns=columns)
        # Setting Period date as index
        df.set_index('Period', inplace=True)
        return df

# Service companies subclass
class ServiceSector(Company):
    def __init__(
        self, date_record,
        total_fee_rev = 0, equity_partner_num = 0, consultant_num = 0, 
        cash = 0, account_receivables = 0, inventory = 0, current_assets = 0, 
        noncurrent_assets  = 0, accu_depr = 0, 
        intangible_assets = 0, longterm_investments = 0, 
        current_lia = 0, noncurrent_lia = 0, 
        owners_equity = 0, net_income  = 0, ebit = 0, 
        total_rev = 0, sales_rev  = 0, total_exp = 0, operating_exp = 0, interest_exp = 0, depr_exp = 0, wages_exp = 0
        ):
        
        # Intializing subclass attributes
        self.total_fee_rev = total_fee_rev
        self.equity_partner_num = equity_partner_num
        self.consultant_num = consultant_num

        # initialize attributes from the base class within the subclasses
        super().__init__(
        date_record
        , cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        )
    
    # Specific Financial Ratios methods
    # profit margin per partner
    def profit_marg_partner(self):
        try:
            return self.net_income / self.equity_partner_num
        except ZeroDivisionError:
            return 0
    # fees revenue per consultant or lawyer
    def fee_rev_consultant_ratio(self):
        try:
            return self.total_fee_rev / self.consultant_num
        except ZeroDivisionError:
            return 0
    # Initiate a dataframe for instance, to be used for 
    def create_df(self):
        # Gathering data in single list
        list_ratios = [
            self.date_record,
            self.profit_marg_partner(), self.fee_rev_consultant_ratio(), # specific methods
            # default methods
            self.current_ratio(), self.quick_ratio(), self.cash_ratio(), # liquidity ratios
            self.total_debt_ratio(), self.dept_equity_ratio(), self.equity_multi(), self.tie(), self.cash_cov_ratio(), # financial leverage ratios
            self.rece_trnovr(), self.days_sales_rece_trnover(), self.total_asset_trnovr(), # turnover ratios 
            self.profit_marg(), self.return_assets(), self.return_equity(), self.wages_rev_ratio() # profitability ratios
        ]
        # Creating a list of column names
        columns = [
            'Period'
            , 'Profit Margin per Partner', 'Fee Revenue per Consultant' # service sector specific ratios
            , 'Current Ratio', 'Quick ratio', 'Cash Ratio' # liquidity ratios
            , 'Total Debt Ratio', 'Debt to Equity', 'Equity Multiplier', 'Times Interest Earned', 'Cash Coverage' # financial leverage ratios
            , 'Receivables Turnover', 'Days sales Receivables Turnover', 'Total Assets Turnover' # turnover ratios
            , 'Profit Margin', 'Return on Assets', 'Return on Equity', 'Payroll(wages) to Revenue' # profitability ratios
        ]  
        # Creating dataframe from values under respective columns
        df = pd.DataFrame([list_ratios], columns=columns)
        # Setting Period date as index
        df.set_index('Period', inplace=True)
        return df

# Manufacturing companies subclass
class Manuf(Company):
    def __init__(
        self, date_record, 
        mtrils_cost = 0, cogs = 0, manuf_cost = 0, 
        cash = 0, account_receivables = 0, inventory = 0, current_assets = 0, 
        noncurrent_assets  = 0, accu_depr = 0, 
        intangible_assets = 0, longterm_investments = 0, 
        current_lia = 0, noncurrent_lia = 0, 
        owners_equity = 0, net_income  = 0, ebit = 0, 
        total_rev = 0, sales_rev  = 0, total_exp = 0, operating_exp = 0, interest_exp = 0, depr_exp = 0, wages_exp = 0  
        ):

        # Initializing subclass attributes
        self.mtrils_cost = mtrils_cost
        self.cogs = cogs
        self.manuf_cost = manuf_cost

        # initialize attributes from the base class within the subclasses
        super().__init__(
        date_record
        , cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        )
    
    # Specific Financial Ratios methods
    # Inventory turnover
    def inv_trnovr(self):
        try:
            return self.cogs / self.inventory
        except ZeroDivisionError:
            return 0
    # Manufacturing costs to expenses ratio
    def manuf_cost_exp_ratio(self):
        try:
            return self.manuf_cost / self.total_exp
        except ZeroDivisionError:
            return 0
    # Materials costs to expenses ratio
    def mtrils_cost_exp_ratio(self):
        try:
            return self.mtrils_cost / self.total_exp
        except ZeroDivisionError:
            return 0
    # Create DataFrame
    # initiate a dataframe for instance, to be used for 
    def create_df(self):
        # Gathering data in single list
        list_ratios = [
            self.date_record,
            self.inv_trnovr(), self.manuf_cost_exp_ratio(), self.mtrils_cost_exp_ratio(), # specific methods
            # default methods
            self.current_ratio(), self.quick_ratio(), self.cash_ratio(), # liquidity ratios
            self.total_debt_ratio(), self.dept_equity_ratio(), self.equity_multi(), self.tie(), self.cash_cov_ratio(), # financial leverage ratios
            self.rece_trnovr(), self.days_sales_rece_trnover(), self.total_asset_trnovr(), # turnover ratios 
            self.profit_marg(), self.return_assets(), self.return_equity(), self.wages_rev_ratio() # profitability ratios
        ]
        # Creating a list of column names
        columns = [
            'Period'
            , 'Inventory Turnover', 'Manufacturing Cost to Expenses Ratio', 'Materials Cost to Expenses Ratio' # manufacturing specific ratios
            , 'Current Ratio', 'Quick ratio', 'Cash Ratio' # liquidity ratios
            , 'Total Debt Ratio', 'Debt to Equity', 'Equity Multiplier', 'Times Interest Earned', 'Cash Coverage' # financial leverage ratios
            , 'Receivables Turnover', 'Days\' sales Receivables Turnover', 'Total Assets Turnover' # turnover ratios
            , 'Profit Margin', 'Return on Assets', 'Return on Equity', 'Payroll(wages) to Revenue' # profitability ratios
        ]  
        # Creating dataframe from values under respective columns
        df = pd.DataFrame([list_ratios], columns=columns)
        # Setting Period date as index
        df.set_index('Period', inplace=True)
        return df    

# Mining and forestry companies subclass
class MiningForestry(Company):
    def __init__(
        self, date_record,
        accu_depl = 0, depl_exp = 0, 
        cash = 0, account_receivables = 0, inventory = 0, current_assets  = 0, 
        noncurrent_assets  = 0, accu_depr  = 0, 
        intangible_assets = 0, longterm_investments  = 0, 
        current_lia = 0, noncurrent_lia  = 0, 
        owners_equity = 0, net_income  = 0, ebit   = 0, 
        total_rev = 0, sales_rev  = 0, total_exp = 0, operating_exp = 0, interest_exp = 0, depr_exp = 0, wages_exp = 0
        ):
        
        # initialize attributes from the base class within the subclasses
        super().__init__(
        date_record
        , cash, account_receivables, inventory, current_assets 
        , noncurrent_assets , accu_depr 
        , intangible_assets, longterm_investments 
        , current_lia, noncurrent_lia 
        , owners_equity, net_income , ebit  
        , total_rev, sales_rev , total_exp, operating_exp, interest_exp, depr_exp, wages_exp  
        )
        
        # Initializing subclass attributes
        self.accu_depl = accu_depl
        self.depl_exp = depl_exp
        
    # Total assets after accumulated depletion
    def total_assets(self):
        return self.cash + self.account_receivables + self.inventory +self.noncurrent_assets + self.current_assets + self.intangible_assets + self.longterm_investments - self.accu_depr - self.accu_depl
    
    # Ignored inherited methods that included `total_assets()` due to change in the calculation of assets (subtracting accumulated depletion)
    # ignored inherited method `cash_cov_ratio` due to adding depl exp
    # -- Total dept ratio
    def total_debt_ratio(self):
        try:
            return (self.total_assets() - self.owners_equity) / self.total_assets()
        except ZeroDivisionError:
            return 0
    # -- Equity Multiplier
    def equity_multi(self):
        try:
            return self.total_assets() / self.owners_equity
        except ZeroDivisionError:
            return 0
    #  -- Total asset turnover
    def total_asset_trnovr(self):
        try:
            return self.sales_rev / self.total_assets()
        except ZeroDivisionError:
            return 0
    # -- Return on assets
    def return_assets(self):
        try:
            return self.net_income / self.total_assets()
        except ZeroDivisionError:
            return 0
    # -- Cash Coverage Ratios
    def cash_cov_ratio(self):
        try:
            return (self.ebit + self.depr_exp + self.depl_exp) / self.interest_exp
        except ZeroDivisionError:
            return 0
    # initiate a dataframe for instance to be used for adding functionality in functionsMod
    def create_df(self):
        # Gathering data in single list
        list_ratios = [
            self.date_record,
            # adjusted financial leverage ratios
            self.total_debt_ratio(), self.equity_multi(), self.total_asset_trnovr(), self.return_assets(), self.cash_cov_ratio(),
            # inherited methods from base class
            self.current_ratio(), self.quick_ratio(), self.cash_ratio(), # liquidity ratios
            self.rece_trnovr(), self.days_sales_rece_trnover(), self.total_asset_trnovr(), # turnover ratios
            self.profit_marg(), self.return_assets(), self.return_equity(), self.wages_rev_ratio() # profitability ratios]
        ]
        # Creating a list of column names
        columns = [
            'Period'
            , 'Total Debt Ratio', 'Equity Multiplier', 'Total Assets Turnover', 'Return on Assets', 'Cash Coverage' # adjusted financial leverage ratios
            , 'Current Ratio', 'Quick ratio', 'Cash Ratio' # liquidity ratios
            , 'Receivables Turnover', 'Days\' sales Receivables Turnover', 'Total Assets Turnover' # turnover ratios
            , 'Profit Margin', 'Return on Assets', 'Return on Equity', 'Payroll(wages) to Revenue' # profitability ratios
        ]  
        # Creating dataframe from values under respective columns
        df = pd.DataFrame([list_ratios], columns=columns)
        # Setting Period date as index
        df.set_index('Period', inplace=True)
        return df
