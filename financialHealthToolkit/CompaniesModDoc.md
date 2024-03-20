### Module Documentation (genAi generated)
#### Purpose:
This module provides a class structure for analyzing company metrics and calculating key performance indicators (KPIs) across various sectors.

#### Class `Company`:
This class serves as a foundation for analyzing financial metrics across different types of businesses. 
It contains attributes representing various financial aspects such as assets, liabilities, equity, income, and expenses. 
Additionally, it provides methods to calculate total assets, total liabilities, liquidity ratios, financial leverage ratios, turnover measures, and profitability measures.

##### Attributes:
- `cash`: Amount of cash on hand.
- `account_receivables`: Amount expected to be received from customers.
- `inventory`: Value of goods held for resale.
- `current_assets`: Total current assets.
- `noncurrent_assets`: Total non-current assets.
- `accu_depr`: Accumulated depreciation.
- `intangible_assets`: Value of intangible assets.
- `longterm_investments`: Value of long-term investments.
- `current_lia`: Total current liabilities.
- `noncurrent_lia`: Total non-current liabilities.
- `owners_equity`: Equity of the company.
- `net_income`: Net income of the company.
- `ebit`: Earnings before interest and taxes.
- `total_rev`: Total revenue.
- `sales_rev`: Revenue from sales.
- `total_exp`: Total expenses.
- `operating_exp`: Operating expenses.
- `interest_exp`: Interest expenses.
- `depr_exp`: Depreciation expenses.
- `wages_exp`: Wages expenses.
- `date_record`: Date of record for the financial metrics.

##### Methods:
- `total_assets()`: Calculates the total assets of the company.
- `total_lia()`: Calculates the total liabilities of the company.
- Liquidity Ratios:
  - `current_ratio()`: Calculates the current ratio.
  - `quick_ratio()`: Calculates the quick ratio.
  - `cash_ratio()`: Calculates the cash ratio.
- Financial Leverage:
  - `total_debt_ratio()`: Calculates the total debt ratio.
  - `dept_equity_ratio()`: Calculates the debt-equity ratio.
  - `equity_multi()`: Calculates the equity multiplier.
  - `tie()`: Calculates the times interest earned ratio.
  - `cash_cov_ratio()`: Calculates the cash coverage ratio.
- Turnover Measures:
  - `rece_trnovr()`: Calculates receivables turnover.
  - `days_sales_rece_trnover()`: Calculates days' sales in receivables.
  - `total_asset_trnovr()`: Calculates total asset turnover.
- Profitability Measures:
  - `profit_marg()`: Calculates the profit margin.
  - `return_assets()`: Calculates the return on assets.
  - `return_assets()`: Calculates the return on equity.
  - `wages_rev_ratio()`: Calculates the wages to revenue ratio.

#### Subclasses:
The module also includes subclasses tailored to specific industries, 
inheriting attributes and methods from the `Company` class while adding industry-specific attributes and methods for more targeted financial analysis.

- `Hotel`: Subclass for analyzing metrics specific to the hotel industry.
- `Trade`: Subclass for analyzing metrics specific to trade businesses.
- `Agriculture`: Subclass for analyzing metrics specific to agricultural businesses.
- `ServiceSector`: Subclass for analyzing metrics specific to service sector businesses.
- `Manuf`: Subclass for analyzing metrics specific to manufacturing companies.
- `mining_forestry`: Subclass for analyzing metrics specific to mining and forestry businesses.

Each subclass includes specific attributes and methods relevant to its respective industry for more detailed financial analysis.

This module provides a versatile framework for analyzing financial metrics and KPIs tailored to different sectors, 
aiding in comprehensive financial assessment and decision-making processes.
