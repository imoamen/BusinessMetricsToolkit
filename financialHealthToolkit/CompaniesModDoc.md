# companyMod Module

This module provides classes for analyzing financial data of various types of companies, including hotels, trade companies, agriculture businesses, service sector companies, manufacturing companies, and mining/forestry companies.

## Classes

### Company

Represents a base class for all types of companies.

#### Attributes

- `cash`: Float, amount of cash held by the company.
- `account_receivables`: Float, value of accounts receivables.
- `inventory`: Float, value of inventory.
- `current_assets`: Float, value of current assets.
- `noncurrent_assets`: Float, value of non-current assets.
- `accu_depr`: Float, accumulated depreciation.
- `intangible_assets`: Float, value of intangible assets.
- `longterm_investments`: Float, value of long-term investments.
- `current_lia`: Float, value of current liabilities.
- `noncurrent_lia`: Float, value of non-current liabilities.
- `owners_equity`: Float, value of owners' equity.
- `net_income`: Float, net income.
- `ebit`: Float, earnings before interest and taxes.
- `total_rev`: Float, total revenue.
- `sales_rev`: Float, revenue from sales.
- `total_exp`: Float, total expenses.
- `operating_exp`: Float, operating expenses.
- `interest_exp`: Float, interest expenses.
- `depr_exp`: Float, depreciation expenses.
- `wages_exp`: Float, wages expenses.
- `date_record`: String, date of the financial record.

#### Methods

- `total_assets()`: Calculates the total assets of the company.
- `total_lia()`: Calculates the total liabilities of the company.

##### Financial ratios methods
- `current_ratio()`: Calculates the current ratio.
- `quick_ratio()`: Calculates the quick ratio.
- `cash_ratio()`: Calculates the cash ratio.
- `total_debt_ratio()`: Calculates the total debt ratio.
- `dept_equity_ratio()`: Calculates the debt to equity ratio.
- `equity_multi()`: Calculates the equity multiplier.
- `tie()`: Calculates the times interest earned ratio.
- `cash_cov_ratio()`: Calculates the cash coverage ratio.
- `rece_trnovr()`: Calculates the receivables turnover.
- `days_sales_rece_trnover()`: Calculates the days' sales in receivables turnover.
- `total_asset_trnovr()`: Calculates the total asset turnover.
- `profit_marg()`: Calculates the profit margin.
- `return_assets()`: Calculates the return on assets.
- `return_equity()`: Calculates the return on equity.
- `wages_rev_ratio()`: Calculates the ratio of wages expenses to total revenue.

#### additional methods
- `create_df()`: Generates a DataFrame with financial ratios for the company. Basis for further analysis

### Hotel, Trade, Agriculture, ServiceSector, Manuf, MiningForestry

### Hotel

Subclass of Company, tailored for hotels.

#### Additional Attributes

- `room_num_aval`: Integer, number of rooms available.
- `room_rev`: Float, revenue generated from room sales.
- `room_num_occ`: Integer, number of rooms occupied.
- `room_num_sold`: Integer, number of rooms sold.
...

#### Additional Methods

- `GOP()`: Calculates the gross operating profit.
- `occ_rate()`: Calculates the occupancy rate.
- `ave_daily_rate()`: Calculates the average daily room rate.
- `rev_per_room_aval()`: Calculates revenue per available room.
- `GOPPAR()`: Calculates gross operating profit per available room.
- `rev_par()`: Calculates revenue per available rooms.
- `create_df()`: Generates a DataFrame with financial ratios specific to hotels.

### Trade

Subclass of Company, tailored for trade companies.

#### Additional Attributes

- `cogs`: Float, cost of goods sold.
- `ave_inv`: Float, average inventory value.

#### Additional Methods

- `inv_trnovr()`: Calculates inventory turnover.
- `days_sales_inv_trnovr()`: Calculates days' sales in inventory turnover.
- `create_df()`: Generates a DataFrame with financial ratios specific to trade companies.

### Agriculture

Subclass of Company, tailored for agriculture businesses.

#### Additional Attributes

- `total_farm_area`: Float, total area of farms.
- `total_farm_rev`: Float, total revenue generated from farming.
- `total_num_stock`: Integer, total number of livestock.
- `total_stock_rev`: Float, total revenue generated from livestock.
...

#### Additional Methods

- `land_yield()`: Calculates yield per unit of farm area.
- `livestock_yield()`: Calculates yield per livestock.
- `create_df()`: Generates a DataFrame with financial ratios specific to agriculture businesses.

### ServiceSector

Subclass of Company, tailored for service sector companies.

#### Additional Attributes

- `total_fee_rev`: Float, total fee revenue.
- `equity_partner_num`: Integer, number of equity partners.
- `consultant_num`: Integer, number of consultants.
...

#### Additional Methods

- `profit_marg_partner()`: Calculates profit margin per partner.
- `fee_rev_consultant_ratio()`: Calculates fee revenue per consultant.
- `create_df()`: Generates a DataFrame with financial ratios specific to service sector companies.

### Manuf

Subclass of Company, tailored for manufacturing companies.

#### Additional Attributes

- `mtrils_cost`: Float, cost of materials.
- `manuf_cost`: Float, manufacturing cost.
...

#### Additional Methods

- `inv_trnovr()`: Calculates inventory turnover.
- `manuf_cost_exp_ratio()`: Calculates manufacturing cost to expenses ratio.
- `mtrils_cost_exp_ratio()`: Calculates materials cost to expenses ratio.
- `create_df()`: Generates a DataFrame with financial ratios specific to manufacturing companies.

### MiningForestry

Subclass of Company, tailored for mining and forestry companies.

#### Additional Attributes

- `accu_depl`: Float, accumulated depletion.
- `depl_exp`: Float, depletion expense.
...

#### Additional Methods

- `total_assets()`: Calculates total assets after considering accumulated depletion.
- `total_debt_ratio()`: Calculates total debt ratio considering accumulated depletion.
- `equity_multi()`: Calculates equity multiplier considering accumulated depletion.
- `total_asset_trnovr()`: Calculates total asset turnover considering accumulated depletion.
- `cash_cov_ratio()`: Calculates cash coverage ratio considering depletion expense.
- `create_df()`: Generates a DataFrame with financial ratios specific to mining and forestry companies.

## Usage

```python
# Import the module
import companyMod

# Create instances of company subclasses
hotel = companyMod.Hotel(...)
trade = companyMod.Trade(...)
...

# Generate DataFrames for analysis
hotel_df = hotel.create_df()
trade_df = trade.create_df()
...
# or import multi_period_table() from functionsMod to combine different periods in one table
# - Create instances of company objects for different periods
company_period1 = cm.Hotel(...)
company_period2 = cm.Hotel(...)
...

# - Concatenate the financial data from different periods
combined_df = multi_period_table(company1, company2, ...)
