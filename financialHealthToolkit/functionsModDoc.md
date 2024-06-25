# Financial Ratios Analysis

This module contains a collection of functions that operate on company instances from the `companyMod` module. These functions vary in usage and are sometimes interdependent; some manipulate DataFrames while others create plots, etc.

## Dependencies

- pandas (pd)
- matplotlib (plt)
- numpy (np)
- companyMod (cm)

## Functions

### multi_period_table(*in_objs)

Concatenates (merges) multiple instances of a company (different periods).

**Parameters:**

- `*in_objs`: Multiple instances of `cm.Company`.

**Returns:**

- A DataFrame containing all periods entered.

**Example:**

```python
df_multi_period = multi_period_table(company1, company2, company3)
```
---

### plt_single_ratio(*in_obj)

Plots a single ratio chosen by the user.

**Parameters:**

- `*in_obj`: Multiple instances of `cm.Company`.

**Usage:**

- The user will be prompted to input the ratio they want to plot.
- Valid ratio names include:
  - Liquidity Ratios: `Current Ratio`, `Quick Ratio`, `Cash Ratio`
  - Financial Leverage Ratios: `Total Debt Ratio`, `Debt to Equity Ratio`, `Equity Multiplier`, `Times Interest Earned`, `Cash Coverage`
  - Turnover Ratios: `Receivables Turnover`, `Days Sales Receivables Turnover`, `Total Assets Turnover`
  - Profitability Ratios: `Profit Margin`, `Return on Assets`, `Return on Equity`, `Payroll(wages) to Revenue Ratio`
  - Hotel Ratios: `GOPPAR`, `Revenue per Available Room`, `Revenue Per Available Rooms`
  - Trade Ratios: `Inventory Turnover`, `Days Sales Inventory Turnover`
  - Farm Ratios: `Land Yield`, `Livestock Yield`
  - Consultancy Ratios: `Profit Margin per Partner`, `Fee Revenue per Consultant`
  - Manufacturing Ratios: `Inventory Turnover`, `Manufacturing Cost to Expenses Ratio`, `Materials Cost to Expenses Ratio`

**Example:**

```python
plt_single_ratio(company1, company2)
```
---

### plt_ratios(*in_objs)

Plots a specific category of ratios chosen by the user.

**Parameters:**

- `*in_objs`: Multiple instances of `cm.Company`.

**Usage:**

- The user will be prompted to input the category of ratios they want to plot.
- Valid categories include:
  - Liquidity Ratios: `liquidity ratios` or `l`
  - Financial Leverage Ratios: `financial leverage` or `f`
  - Turnover Ratios: `turnover ratios` or `t`
  - Profitability Ratios: `profitability ratios` or `p`

**Example:**

```python
plt_ratios(company1, company2)
```

**Notes:**

- For both plotting functions, the user will be prompted to input whether they want to create another plot after each plot is generated.
- The program handles various input errors, guiding the user to enter valid ratio names or categories.
