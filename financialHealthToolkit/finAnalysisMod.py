import functionsMod as fm 
import numpy as np 
# this file performes diagnosic financial analysis on instances of `cm.company`, the asses liquidity, profitability, leverage, etc..., 
# the diagnosis itself is based on the sources mentioned in README file in the `financialHeathToolkit`,
# the functions provide diagnostics based on the data from different periods
# all functions here expect instances of `cm.company`'s subclasses.
# The `numpy` library for arrays for there speed and efficiency and the ability to perform complex mathimatical operations not available in standard py data structures
# -------------------------------------------------------------------------------------------------------------------------------------------------------
#                                            *** Some algorithms used in this model ***
# the algorithms are explained in detail before the code here and another time in the code only the first time it is used
'''
A. "outlier values (bad ratios) weed out"
    # When used in a function, it will have the name of the algorithm commented besides it
    this algorithm goes as follows:
    1. iterating on entered objects (different periods)
    2. when finding a ratio below or above or equal to a set benchmark the program records the period date in a list
    3. once at least one is found, meaning the list is no longer empty we set a variable to True
    4. at the condition the variable is true a diagnosis is printed

B. "time-trend analysis"
    one algorithm that was used to assess ratios at different yet chronological periods goes like this:
    # When used in a function, it will have the name of the algorithm commented besides it
        1. we call a function in functionsMod called `muli_period_table()`, it returns a data frame of all 
            periods needed with periods (date of recording) as indices and ratios as columns.
        2. Iterate through the objects and append the desired ratio at each period in order in an array.
        3. Create another array that is populated by the difference between each element and the one before it.
        4. Calculating the average rate of change.
        5. Provide diagnsis based on the sign of the averge rate of change.

C.
'''
# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Main function that analyzes liquidity data
# All innerfunctions just print the diagnosis, when the user runs the functions the only thing they get is a printed diagnosis
def liquidity_analysis(*in_objs):
    
    # *checks whether the current ratio at any period was less than or equal to one (a bad thing)
    def crrnt_ratio_weedout(*in_objs): # bad ratio weed out
        
        bad_ratios_list = [] # create an empty list 
        atleast_one_bad_ratio = False # and a variable that is False
        for period in in_objs: # for every object in all entered objects if the period has a less than or equal to 
            
            if period.current_ratio() <= 1: # `current_ratio` is a method that the entered instances inherits from `cm.company` that calculates the ratio from the instance's attributes
                bad_ratios_list.append(period.date_record) # and append the period date in the empty list
                atleast_one_bad_ratio = True  # and set the variable to true
        
        if atleast_one_bad_ratio: # given that the variable came true then this executes and prints a prescription
            the_bad_periods = str(bad_ratios_list)
            dignosis_bad_ratio = f'''\n         *** Dignosis Related to analysis of the company's current ratio ***
            \nBad current ratios found in {the_bad_periods}
            \n-----------------------------------------------------------------------------------------------
            \nHigh shot-term debt!!! in mentioned periods. 
            \nAbsent some extraordinary circumstances,
            \nwe would expect to see a current ratio of at least 1 because a current ratio of 
            \nless than 1 would mean that net working capital (current assets less current liabilities) is 
            \nnegative. This would be unusual in a healthy firm, at least for most types of businesses.
            '''
            print(dignosis_bad_ratio)


    # What kind of Time-trends does the provided objects' current ratio exhibit?
    def crrnt_ratio_time_analysis(*in_objs): # Time-trend analysis
        ratios_df = fm.multi_period_table(*in_objs) # store a data frame of all ratios in all periods provided in one variable
        ratios_array = np.array([]) # To iterate on the different objects (periods) in the argument we create an empty array

        for period in in_objs: # for every period entered
            # append the current ratio at every date in the empty array
            # after the iteration we are left with an array that holds all the current ratio for evry period
            ratios_array = np.append(ratios_array, ratios_df.loc[str(period.date_record), 'Current Ratio'])
        
        inst_slope_array = np.array([]) # we then iterate on that but first we create yet another empty np array
        for i in range(len(ratios_array)-1):
            # we then subtract each value by the noe before it calculating -subsequently- the instantaneous rate of change (the slope)
            # the number of times we iterate is equal to the length of the array minus one
            # i.e. if the array is [a, b, c] given they be numbers then we need to subtract: c-b, b-a i.e. 2 slopes when the length was 3
            # we also need to accout for indexing starting from zero, that is dealt with because of `range()`'s non-inclusive property 
            # so if the length is lets say 3, i start at 0 and ends with 1, so, 
            # 1. the first iteration subtracts value with index i+1 which is 1 which is the second from i which is 0 meaning the first element: (b-a)
            # 2. then we subtract i+1 now 2 which is the third from the second: (c-b).
            #combining 1 and 2, the array --> [(b-a), (c-b)]
            inst_slope_array = np.append(inst_slope_array, ratios_array[i+1] - ratios_array[i])
        
        ave_slope = np.average(inst_slope_array)
        
        if ave_slope != abs(ave_slope): # if the average slope is neagative the ratio is decreasing and diagnosis is then printed.
            dignosis = '''\n
            \n-----------------------------------------------------------------------------------------------
            \n*** Dignosis Related to time trend analysis of the company's current ratio ***
            \nIdentified a pattern of decreasing current ratio;
            \nthis indicates an unhealthy trend of decreasing of short-term liquidity.
            \nfor investors, this could mean that the company could soon have trouble paying it's short term debts.
            \nNote that an apparently low current ratio may not be a bad sign for a company 
            \nwith a large reserve of untapped borrowing power.
            '''
        
        else: # positive slope needs some explaination too, here it is
             dignosis = '''\n
             \n-----------------------------------------------------------------------------------------------
             \n*** Dignosis Related to time trend analysis of the company's current ratio ***
             \nIdentified a pattern of increasing current ratio, 
             \nTo the firm, a high current ratio indicates liquidity, 
             \nbut it also may indicate an inefficient use of cash and other short-term assets.
             \nBoth investors and creditors prefer seeing higher current ratios.
             '''
        
        print(dignosis)
    

    # What kind of Time-trends does the provided objects' cash ratio exhibit?
    def csh_ratio_time_analysis(*in_objs): # Time-trend analysis
        
        ratios_df = fm.multi_period_table(*in_objs)
        
        ratios_array = np.array([])
        for ratio in in_objs:
                ratios_array = np.append(ratios_array, ratios_df.loc[str(ratio.date_record), 'Cash Ratio'])
        
        inst_slope_array = np.array([])
        for i in range(len(ratios_array)-1):
            inst_slope_array = np.append(inst_slope_array, ratios_array[i+1] - ratios_array[i])
        
        ave_slope = np.average(inst_slope_array)
        
        if ave_slope != abs(ave_slope):
            dignosis = '''\n
            \n-----------------------------------------------------------------------------------------------
            \n*** Dignosis Related to time trend analysis of the company's Cash Ratio ***
            \nIdentified a pattern of decreasing cash ratio!!!,
            \nThis means decreasing liquidity which in term indicates that, 
            \nthe firm is more and more likely to struggle to fulfill short-term obligatons
            '''
        
        else:
             dignosis = '''\n
            \n-----------------------------------------------------------------------------------------------
            \n*** Dignosis Related to time trend analysis of the company's Cash Ratio ***
            \nIdentified a pattern of increasing cash ratio!!!, A generally positive sign.
            '''
        
        print(dignosis)

    crrnt_ratio_weedout(*in_objs)
    crrnt_ratio_time_analysis(*in_objs)
    csh_ratio_time_analysis(*in_objs)


# Main function that analyzes liquidity data
# All innerfunctions just print the diagnosis, when the user runs the functions the only thing they get is a printed diagnosis
def financial_leverage_analysis(*in_objs):
    
    # *checks whether the times interest earned at any period was less than or equal to one (a bad thing)
    # To iterate on the different objects (periods) in the argument we: 
    def tie_weedout(*in_objs):
        bad_ratios_list = [] 
        atleast_one_bad_ratio = False 
        for period in in_objs: 
            
            if period.tie() <= 1: # `tie` is a method that the entered instances inherits from `cm.company` that calculates the ratio from the instance's attributes
                bad_ratios_list.append(period.date_record) 
                atleast_one_bad_ratio = True  
        
        if atleast_one_bad_ratio: 
            the_bad_periods = str(bad_ratios_list)
            dignosis_bad_ratio = f'''\n         *** Dignosis Related to analysis of the company's Times Iinterest Earned ratio ***
            \nBad tie ratios found in {the_bad_periods}
            \n-----------------------------------------------------------------------------------------------
            \nHigh TIE!!! in mentioned periods. 
            \nAbsent some extraordinary circumstances,
            \nwe would expect to see a ties of at least 1 because a tie of 
            \nless than 1 would mean that the firm is behind in regards to payin g back accured interest  
            \nThis would be unusual in a healthy firm, at least for most types of businesses.
            '''
            
            print(dignosis_bad_ratio)
    

    # *checks whether the times interest earned at any period was less than or equal to one (a bad thing)
    def csh_cvrg_weedout(*in_objs):
        bad_ratios_list = [] 
        atleast_one_bad_ratio = False 
        for period in in_objs: 
            
            if period.cash_cov_ratio() <= 1: # `cash_cov_ratio` is a method that the entered instances inherits from `cm.company` that calculates the ratio from the instance's attributes
                bad_ratios_list.append(period.date_record) 
                atleast_one_bad_ratio = True  
        
        if atleast_one_bad_ratio: 
            the_bad_periods = str(bad_ratios_list)
            dignosis_bad_ratio = f'''\n         *** Dignosis Related to analysis of the company's Cash Coverage ratio ***
            \nBad cash coverage ratios found in {the_bad_periods}
            \n-----------------------------------------------------------------------------------------------
            \nLow cash coverage!!! in mentioned periods. 
            \nAbsent some extraordinary circumstances,
            \nwe would expect to see a cash coverage of at least 1 because a cash coverage of 
            \nless than 1 would mean that the firm is behind in regards to payin g back accured interest  
            \nThis would be unusual in a healthy firm, at least for most types of businesses.
            '''
            
            print(dignosis_bad_ratio)
    
    # What kind of Time-trends does the provided objects' current ratio exhibit?
    def tdbt_time_analysis(*in_objs): # Time-trend analysis
        
        ratios_df = fm.multi_period_table(*in_objs)
        
        ratios_array = np.array([])
        for ratio in in_objs:
                ratios_array = np.append( ratios_array, ratios_df.loc[str(ratio.date_record), 'Total Debt Ratio'])
        
        inst_slope_array = np.array([])
        for i in range(len( ratios_array)-1):
            inst_slope_array = np.append(inst_slope_array, ratios_array[i+1] - ratios_array[i])
        
        ave_slope = np.average(inst_slope_array)
        
        if ave_slope != abs(ave_slope):
            dignosis = '''\n
            \n-----------------------------------------------------------------------------------------------
            \n*** Dignosis Related to time trend analysis of the company's Total Debt Ratio ***
            \nIdentified a pattern of decreasing Total Debt Ratio ratio
            \n'''
        
        else:
             dignosis = '''\n
            \n-----------------------------------------------------------------------------------------------
            \n*** Dignosis Related to time trend analysis of the company's Total Debt Ratio ***
            \nIdentified a pattern of increasing Total Debt Ratio'''
        
        print(dignosis)
    tie_weedout(*in_objs)
    csh_cvrg_weedout(*in_objs)
    tdbt_time_analysis(*in_objs)

# Main function that analyzes turnover data
# All innerfunctions just print the diagnosis, when the user runs the functions the only thing they get is a printed diagnosis
def turnover_analysis(*in_objs):
    # *checks whether the times interest earned at any period was less than or equal to one (a bad thing)
    def rtrn_weedout(*in_objs):
        bad_ratios_list = [] 
        atleast_one_bad_ratio = False 
        for period in in_objs: 
            
            if period.rece_trnovr() <= 1: # `rece_trnovr` is a method that the entered instances inherits from `cm.company` that calculates the ratio from the instance's attributes
                bad_ratios_list.append(period.date_record) 
                atleast_one_bad_ratio = True  
        
        if atleast_one_bad_ratio: 
            the_bad_periods = str(bad_ratios_list)
            dignosis_bad_ratio = f'''\n         *** Dignosis Related to analysis of the company's Receivables Turnover ratio ***
            \nBad Receivables Turnover ratios found in {the_bad_periods}
            \n-----------------------------------------------------------------------------------------------
            \nLow Receivables Turnover!!! in mentioned periods. 
            \nAbsent some extraordinary circumstances,
            \nwe would expect to see a Receivables Turnover of at least 1 because a Receivables Turnover of 
            \nless than 1 would mean that the firm is collecting it's outstanding credit accounts less than
            \none ime every year
            '''
    
            print(dignosis_bad_ratio)

    # What kind of Time-trends does the provided objects' current ratio exhibit?    
    def tatrn_time_analysis(*in_objs): # Time-trend analysis
        
        ratios_df = fm.multi_period_table(*in_objs)
        
        ratios_array = np.array([])
        for ratio in in_objs:
                ratios_array = np.append(ratios_array, ratios_df.loc[str(ratio.date_record), 'Total Assets Turnover'])
        
        inst_slope_array = np.array([])
        for i in range(len(ratios_array)-1):
            inst_slope_array = np.append(inst_slope_array, ratios_array[i+1] - ratios_array[i])
        
        ave_slope = np.average(inst_slope_array)

        if ave_slope != abs(ave_slope):
            dignosis = '''\n
            \n-----------------------------------------------------------------------------------------------
            \n*** Dignosis Related to time trend analysis of the company's Total Asset Turnover ***
            \nIdentified a pattern of decreasing Total Asset Turnover!!!, 
            \nthe firm is more and more likely to struggle to fulfill short-term obligatons
            \nA decreasing number is generally a bad indication espeacially if it is below the industry average (industry averages are not examined here)
            \nIn the exception of company purchased a lot of new (e.g. equipment, facilities, ...), 
            \nwhich implies that the book value of assets is relatively high. 
            \nThese new assets could be more productive and efficient than those used by the company’s competitors.
            '''
        
        else:
             dignosis = '''\n
            \n-----------------------------------------------------------------------------------------------
            \n*** Dignosis Related to time trend analysis of the company's Total Asset Turnover ***
            \nIdentified a pattern of increasing Total Asset Turnover!!!, 
            \nAn Increasing ratio is generally a good indication as long as the company doesn't have a lot of old assets,
            \nwhich means that the assets would be almost fully depreciated and might be very outdated. 
            \nIn this case, the book value of assets is low, contributing to a higher asset turnover. 
            \nPlus, the high turnover might mean that the company will need to make major capital outlays in the near future. 
            '''
        
        print(dignosis)
    rtrn_weedout(*in_objs)
    tatrn_time_analysis(*in_objs)
