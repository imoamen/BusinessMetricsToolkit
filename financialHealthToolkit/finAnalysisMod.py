import functionsMod as fm 
import numpy as np 
# this file performes diagnosic financial analysis on instances of `cm.company`, the asses liquidity, profitability, leverage, etc..., 
# the diagnosis itself is based on the sources mentioned in `metricsSources.md` in the `financialHeathToolkit`,
# the functions provide diagnostics based on the data from different periods
# all functions here expect instances of `cm.company`'s subclasses.
# The `numpy` library for arrays for there speed and efficiency and the ability to perform complex mathimatical operations not available in standard py data structures
# -------------------------------------------------------------------------------------------------------------------------------------------------------
#                                            *** Some algorithms used in this model ***
'''
A. "time-trend analysis"
one algorithm that was used to assess ratios at different yet chronological periods goes like this:
# When used in a function, it will have the name of the algorithm commented besides it
    1. we call a function in functionsMod called `muli_period_table()`, it returns a data frame of all 
        periods needed with periods (date of recording) as indices and ratios as columns.
    2. Iterate through the objects and append the desired ratio at each period in order in an array.
    3. Create another array that is populated by the difference between each element and the one before it.
    4. Calculating the average rate of change.
    5. Provide diagnsis based on the sign of the averge rate of change.
B. 
'''
# --------------------------------------------------------------------------------------------------------------------------------------------------------

# Main function that analyzes liquidity data
# All innerfunctions just print the diagnosis, when the user runs the functions the only thing they get is a printed diagnosis
def liquidity_analysis(*in_objs):
    # checks whether the current ratio from the last period was less then one (a bad thing)
    # If it is it considers it an unsolved problem regardless if other periods had less than one ratios or not
    def crrnt_ratio_health(*in_objs):
        # To iterate on the different objects (periods) in the argument we create an empty list 
        bad_crrnt_list = []
        for period in in_objs:
            # for every object in all entered objects if the period has a less than or equal to append one into the empty list
            if period.current_ratio() <= 1: # `current_ratio` is a method that the entered instances inherits from `cm.company` that calculates the ratio from the instance's attributes
                bad_crrnt_list.append(1)
            # else append zero to the empty list
            else:
                 bad_crrnt_list.append(0)
        # whatever the last appended number is, store it in `last_crrnt_ratio`
        last_crrnt_ratio = bad_crrnt_list[-1]
        # if the last value of the now populated list is one (meaning the ratio is less than or equal to one)
        # --> print the diagnosis for that
        if last_crrnt_ratio == 1:
            dignosis_bad_ratio = '''\n
            \n-----------------------------------------------------------------------------------------------
            \n*** Dignosis Related to analysis of the company's current ratio ***
            \nUnresolved High shot-term debt!!! in the last period. 
            \nAbsent some extraordinary circumstances,
            \nwe would expect to see a current ratio of at least 1 because a current ratio of 
            \nless than 1 would mean that net working capital (current assets less current liabilities) is 
            \nnegative. This would be unusual in a healthy firm, at least for most types of businesses.
            '''
            print(dignosis_bad_ratio)

    # What kind of Time-trends does the provided objects' current ratio exhibit?
    def crrnt_ratio_time_analysis(*in_objs): # Time-trend analysis
        # store a data frame of all ratios in all periods provided in one variable
        ratios_df = fm.multi_period_table(*in_objs)
        # To iterate on the different objects (periods) in the argument we create an empty array
        crrnt_array = np.array([])
        # for every period entered
        for period in in_objs:
            # append the current ratio at every date in the empty array
            # after the iteration we are left with an array that holds all the current ratio for evry period
            crrnt_array = np.append(crrnt_array, ratios_df.loc[str(period.date_record), 'Current Ratio'])
        # we then iterate on that but first we create yet another empty np array
        inst_slope_array = np.array([])
        for i in range(len(crrnt_array)-1):
            # we then subtract each value by the noe before it calculating -subsequently- the instantaneous rate of change (the slope)
            # the number of times we iterate is equal to the length of the array minus one
            # i.e. if the array is [a, b, c] given they be numbers then we need to subtract: c-b, b-a i.e. 2 slopes when the length was 3
            # we also need to accout for indexing starting from zero, that is dealt with because of `range()`'s non-inclusive property 
            # so if the length is lets say 3, i start at 0 and ends with 1, so, 
            # the first iteration subtracts value with index i+1 which is 1 which is the second from i which is 0 meanind the first element (b-a)
            # then i+1 now 2 which is the third from the second (c-b).
            inst_slope_array = np.append(inst_slope_array, crrnt_array[i+1] - crrnt_array[i])
        ave_slope = np.average(inst_slope_array)
        # if the average slope is neagative the ratio is decreasing and diagnosis is then printed.
        if ave_slope != abs(ave_slope):
            dignosis_slope_crrnt_ratio = '''\n
            \n-----------------------------------------------------------------------------------------------
            \n*** Dignosis Related to time trend analysis of the company's current ratio ***
            \nIdentified a pattern of decreasing current ratio;
            \nthis indicates an unhealthy trend of decreasing of short-term liquidity.
            \nfor investors, this could mean that the company could soon have trouble paying it's short term debts.
            \nNote that an apparently low current ratio may not be a bad sign for a company 
            \nwith a large reserve of untapped borrowing power.
            '''
        # positive slope needs some explaination too, here it is
        else:
             dignosis_slope_crrnt_ratio = '''\n
             \n-----------------------------------------------------------------------------------------------
             \n*** Dignosis Related to time trend analysis of the company's current ratio ***
             \nIdentified a pattern of increasing current ratio, 
             \nTo the firm, a high current ratio indicates liquidity, 
             \nbut it also may indicate an inefficient use of cash and other short-term assets.
             \nBoth investors and creditors prefer seeing higher current ratios.
             '''
        print(dignosis_slope_crrnt_ratio)
    # What kind of Time-trends does the provided objects' cash ratio exhibit?
    # it goes the same as the last function (Time-trend analysis algorithm):
    def csh_ratio_time_analysis(*in_objs): # Time-trend analysis
        ratios_df = fm.multi_period_table(*in_objs)
        csh_array = np.array([])
        for ratio in in_obj:
                csh_array = np.append(csh_array, ratios_df.loc[str(ratio.date_record), 'Cash Ratio'])
        inst_slope_array = np.array([])
        for i in range(len(csh_array)-1):
            inst_slope_array = np.append(inst_slope_array, csh_array[i+1] - csh_array[i])
        ave_slope = np.average(inst_slope_array)
        if ave_slope != abs(ave_slope):
            dignosis_slope_csh_ratio = '''\n
            \n-----------------------------------------------------------------------------------------------
            \n*** Dignosis Related to time trend analysis of the company's Cash Ratio ***
            \nIdentified a pattern of decreasing cash ratio!!!,
            \nThis means decreasing liquidity which in term indicates that, 
            \nthe firm is more and more likely to struggle to fulfill short-term obligatons
            '''
        else:
             dignosis_slope_csh_ratio = '''\n
            \n-----------------------------------------------------------------------------------------------
            \n*** Dignosis Related to time trend analysis of the company's Cash Ratio ***
            \nIdentified a pattern of increasing cash ratio!!!, A generally positive sign.
            '''
        print(dignosis_slope_csh_ratio)

    crrnt_ratio_health(*in_objs)
    crrnt_ratio_time_analysis(*in_objs)
    csh_ratio_time_analysis(*in_objs)
