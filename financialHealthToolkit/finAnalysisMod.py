import functionsMod as fm 
import numpy as np 

def liquidity_analysis(*in_obj):
    def crrnt_ratio_health(*in_obj):
        bad_crrnt_list = []
        for period in in_obj:
            if period.current_ratio() <= 1:
                bad_crrnt_list.append(1)
            else:
                 bad_crrnt_list.append(0)
        last_crrnt_ratio = bad_crrnt_list[-1]
        if last_crrnt_ratio == 1:
            dignosis_bad_ratio = '''\n
            \n-----------------------------------------------------------------------------------------------
            \n*** Dignosis Related to analysis of the company's current ratio ***
            \nHigh shot-term debt!!!. 
            \nAbsent some extraordinary circumstances,
            \nwe would expect to see a current ratio of at least 1 because a current ratio of 
            \nless than 1 would mean that net working capital (current assets less current liabilities) is 
            \nnegative. This would be unusual in a healthy firm, at least for most types of businesses.
            '''
            print(dignosis_bad_ratio)

    def crrnt_ratio_time_analysis(*in_obj):
        ratios_df = fm.multi_period_table(*in_obj)
        crrnt_array = np.array([])
        for ratio in in_obj:
                crrnt_array = np.append(crrnt_array, ratios_df.loc[str(ratio.date_record), 'Current Ratio'])
        inst_slope_array = np.array([])
        for i in range(len(crrnt_array)-1):
            inst_slope_array = np.append(inst_slope_array, crrnt_array[i+1] - crrnt_array[i])
        ave_slope = np.average(inst_slope_array)
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
        else:
             dignosis_slope_crrnt_ratio = '''\n
             \n-----------------------------------------------------------------------------------------------
             \n*** Dignosis Related to time trend analysis of the company's current ratio ***
             \nIdentified a pattern of increasing current ratio, 
             \nTo the firm, a high current ratio indicates liquidity, 
             \nbut it also may indicate an inefficient use of cash and other short-term assets.
             \nBoth investors and creditors prefer seeing higher current ratio.
             '''
        print(dignosis_slope_crrnt_ratio)

    def csh_ratio_time_analysis(*in_obj):
        ratios_df = fm.multi_period_table(*in_obj)
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

    crrnt_ratio_health(*in_obj)
    crrnt_ratio_time_analysis(*in_obj)
    csh_ratio_time_analysis(*in_obj)





          



