# Financial Ratios Analysis

This module contains a collection of functions that operate on company instances from the `companyMod` module. These functions vary in usage and are sometimes interdependent; e.g. manipulate DataFrames.

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
