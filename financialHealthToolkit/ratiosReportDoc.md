# Financial Ratios display Tool

## Description
This repository contains a Python tool for analyzing financial ratios of different types of companies. The tool is designed to calculate and present various financial ratios and metrics commonly used in financial analysis, tailored to specific industries such as hotels, trade companies, agriculture, service sectors, manufacturing companies, mining, and forestry.

## Features
- Provides a flexible class structure representing different types of companies, each with specific attributes and methods for calculating financial ratios.
- Includes functions to convert financial ratios of different company types into pandas Series objects, facilitating easy analysis and visualization.
- Supports a wide range of financial ratios including liquidity ratios, financial leverage ratios, turnover ratios, and profitability ratios.
- Utilizes inheritance and method overriding to customize calculations and metrics based on the industry type.
- Offers clear and concise documentation for classes, methods, and functions.
  
## Usage
1. Clone the repository to your local machine.
2. Import the necessary modules and classes provided in `companyMod` into your Python environment.
3. Create instances of company objects and utilize the provided functions to analyze their financial ratios.
4. Optionally, customize the tool to add new company types or extend functionality.

## Example
```python
import pandas as pd
import companyMod as cm
import ratiosReport as rr

# Create an instance of a hotel company
hotel_company = cm.Hotel(...)
# run the appropriate function
rr.series_ratios_hotel(hotel_company)
