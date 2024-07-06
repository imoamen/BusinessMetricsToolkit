import functionsMod as fm 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# plots a single ratio chosen by the user
def plt_single_ratio(*in_obj):
    
    ratios_df = fm.multi_period_table(*in_obj)# assigning the dataframe of ratios to 'ratios_df'
    
    pltin_done  = False
    while not pltin_done:
        try:
            
            # list of all ratio names
            ratios_list = ['Current Ratio', 'Quick Ratio', 'Cash Ratio' # liquidity ratios
                , 'Total Debt Ratio', 'Debt to Equity Ratio', 'Equity Multiplier', 'Times Interest Earned', 'Cash Coverage' # financial leverage ratios
                , 'Receivables Turnover', 'Days Sales Receivables Turnover', 'Total Assets Turnover' # turnover ratios
                , 'Profit Margin', 'Return on Assets', 'Return on Equity', 'Payroll(wages) to Revenue Ratio' # profitability ratios
                , 'GOPPAR', 'Revenue per Available Room', 'Revenue Per Available Rooms' # hotel ratios
                , 'Inventory Turnover', 'Days Sales Inventory Turnover' # trade ratios
                , 'Land Yield', 'Livestock Yield' # farm ratios
                , 'Profit Margin per Partner', 'Fee Revenue per Consultant' # consultancy ratios
                , 'Inventory Turnover', 'Manufacturing Cost to Expenses Ratio', 'Materials Cost to Expenses Ratio' # manufacturing Ratios
            ]

            
            single_ratio = str(input('Which ratio do you want to plot? :'))# user enters the name of the ratio they want to plot
            if single_ratio not in ratios_list:# executes if the user enters a string but not a valid ratio name
               
               # shows the user the valid string type ratio names for them to choose from
               print("""Entered ratio was no recognized, make sure your entry was in these:
               \n # liquidity ratios:
               \n 'Current Ratio', 'Quick Ratio', 'Cash Ratio' 
               \n # financial leverage ratios:
               \n 'Total Debt Ratio', 'Debt to Equity Ratio', 'Equity Multiplier', 'Times Interest Earned', 'Cash Coverage' 
               \n # turnover ratios:
               \n 'Receivables Turnover', 'Days Sales Receivables Turnover', 'Total Assets Turnover' 
               \n # profitability ratios:
               \n 'Profit Margin', 'Return on Assets', 'Return on Equity', 'Payroll(wages) to Revenue Ratio' 
               \n # hotel ratios:
               \n 'GOPPAR', 'Revenue per Available Room', 'Revenue Per Available Rooms' 
               \n # trade ratios:
               \n 'Inventory Turnover', 'Days Sales Inventory Turnover' 
               \n # farm ratios:
               \n 'Land Yield', 'Livestock Yield' 
               \n # consultancy ratios:
               \n 'Profit Margin per Partner', 'Fee Revenue per Consultant' 
               \n # manufacturing Ratios:
               \n 'Inventory Turnover', 'Manufacturing Cost to Expenses Ratio', 'Materials Cost to Expenses Ratio' 
               """)

               continue # because there is no need for to ask the user if they want another plot, the didn't make one yet!

            else:# executes if the user enters a valid ratio name 
                
                # the program now plots the ratio based on the arguments entered
                plt.xlabel('Period')# plot the index (which is the periods dates) on the x-axis and the ratio on the y-axis
                plt.ylabel(single_ratio)
                plt.title(f'{single_ratio} over time')
                plt.plot(ratios_df.index, ratios_df[single_ratio].tolist(), 'yo-') # yellow line with dots at each point)
                plt.show()  # Ensure the plot is displayed
            
            while True: # Does the user want another plot made?
                    try:
                        
                        pltin_done_var = input('Do you want to make another plot? y/n: --> ').strip().lower()
                        
                        if pltin_done_var == 'y':# If yes, then break this loop and don't change the value of 'pltin_done'
                            break
                        
                        elif pltin_done_var == 'n':# if no, break the loop and change the value of 'pltin_done' to true to exit the outer loop and end the program
                            pltin_done = True
                            break
                        
                        else:# executes it the user enters an invalid string answer, here the loop isn't broken, rather it reprompts the user and asks them for a valid answer
                            print("Please enter a valid answer:\n 'y' if you want to make another plot\n 'n' if you want to end the program")
                    
                    except ValueError:# executes if the user enters an invalid non-string answer, here the loop isn't broken, rather it reprompt the user and asks them for a valid answer
                        print("Please enter a valid answer:\n 'y' if you want to make another plot\n 'n' if you want to end the program")

        except ValueError: # executes if there is a problem with the argument entered, the execution for the innerfunctions was interupted
            print('Program Failed to plot your data, possible reasons,\n you entered periods of multiple types of companys\n you entered instances of other classes or no objects at all\n *note that the only valid input to this function is an instance of `cm.company` subclasses')
    

            

# plots a specific category of ratios chosen by the user
def plt_ratios(*in_objs):
    # liquidity ratios
    def plt_liq_ratios(*in_objs):
        ratios_df = fm.multi_period_table(*in_objs)
        # plot color, dimensions, and axes
        plt.style.use(['seaborn-v0_8'])
        plt.figure(figsize=(16,8))
        plt.xlabel('Period')
        plt.ylabel('Ratio')
        plt.title('Liquidity ratios over time')

        # creating lines for each graph, they are assigned to variables for futhur use in 'legend()'
        cr_time = plt.plot(ratios_df.index, ratios_df['Current Ratio'],'bo-')
        qr_time = plt.plot(ratios_df.index, ratios_df['Quick Ratio'], 'co-')
        cshr_time = plt.plot(ratios_df.index, ratios_df['Cash Ratio'], 'go-')

        # drawing a horizontal line representing the minimum tie and cash coverage ratios 
        min_cr_time = plt.plot(ratios_df.index, [ 1 for _ in in_objs], 'ko--') # for every period there is, append 1 to the x=axis list
        
        # assigning patch colors to variables for fithur use in 'legend()'
        blgnd = mpatches.Patch(color='blue', label='Current Ratio')
        clgnd = mpatches.Patch(color='cyan', label='Quick Ratio')
        glgnd = mpatches.Patch(color='green', label='Cash Ratio')
        klgnd = mpatches.Patch(color='black', label='Minimum Current Ratio')

        plt.legend([cr_time, qr_time, cshr_time, min_cr_time], # plots needed to label
                   handles = [blgnd, clgnd, glgnd, klgnd], # corresponding handle patch colors
                   bbox_to_anchor=(.675, -0.1), #coordinates of the legend
                   ncol=3, #number of columns the legend handles are arranged to
                   borderaxespad=0.) #border between columns
        
        plt.show() # command to show the plot

    # financial leverage ratios
    def plt_finlev_ratios(*in_objs):
        
        ratios_df = fm.multi_period_table(*in_objs)

        # plot color, dimensions, and axes
        plt.style.use(['seaborn-v0_8'])
        plt.figure(figsize=(16,8))
        plt.xlabel('period')
        plt.ylabel('Ratio')
        plt.title('Financial leverage over time')
        
        # creating lines for each graph, they are assigned to variables for futhur use in 'legend()'
        tdr_time = plt.plot(ratios_df.index, ratios_df['Total Debt Ratio'],'ro-')
        de_time = plt.plot(ratios_df.index, ratios_df['Debt to Equity Ratio'], 'go-')
        em_time = plt.plot(ratios_df.index, ratios_df['Equity Multiplier'], 'bo-')
        tie_time = plt.plot(ratios_df.index, ratios_df['Times Interest Earned'], 'co-')
        cshcov_time = plt.plot(ratios_df.index, ratios_df['Cash Coverage'], 'yo-')

        # drawing a horizontal line representing the minimum tie and cash coverage ratios 
        min_tie_time = plt.plot(ratios_df.index, [1 for _ in in_objs], 'ko--') # for every periiod there is, sppend one to the x-axis list
        
        # assigning patch colors to variables for fithur use in 'legend()'
        rlgnd = mpatches.Patch(color='red', label='Total Debt Ratio')
        blgnd = mpatches.Patch(color='blue', label='Debt to Equity Ratio')
        glgnd = mpatches.Patch(color='green', label='Equity Multiplier')
        clgnd = mpatches.Patch(color='cyan', label='Times Interest Earned')
        ylgnd = mpatches.Patch(color='yellow', label='Cash Coverage')
        klgnd = mpatches.Patch(color='black', label='minimum Times Interest Rate and Cash Coverage Ratios')
        
        plt.legend([tdr_time, de_time, em_time, tie_time, cshcov_time, min_tie_time ], # plots needed to label
                   handles = [rlgnd,  blgnd, glgnd, clgnd, ylgnd, klgnd], # corresponding handle patch colors
                   bbox_to_anchor=(1, -0.1), #coordinates of the legend
                   ncol=5, #number of columns the legend handles are arranged to
                   borderaxespad=0.) #border between columns
        
        plt.show() # command to show the plot
    
    # turnover ratios
    def plt_trnvr_ratios(*in_objs):
        
        ratios_df = fm.multi_period_table(*in_objs)

        # plot color, dimensions, and axes
        plt.style.use(['seaborn-v0_8'])
        plt.figure(figsize=(16,8))
        plt.xlabel('period')
        plt.ylabel('Ratio')
        plt.title('Turnover ratios over time')
        
        # creating lines for each graph, they are assigned to variables for futhur use in 'legend()'
        rtrn_time = plt.plot(ratios_df.index, ratios_df['Receivables Turnover'],'ro-')
        dystrn_time = plt.plot(ratios_df.index, ratios_df['Days Sales Receivables Turnover'], 'go-')
        tatrn_time = plt.plot(ratios_df.index, ratios_df['Total Assets Turnover'], 'bo-')
        
        # assigning patch colors to variables for fithur use in 'legend()'
        rlgnd = mpatches.Patch(color='red', label='Receivables Turnover')
        blgnd = mpatches.Patch(color='blue', label='Days Sales Receivables Turnover')
        glgnd = mpatches.Patch(color='green', label='Total Assets Turnover')
        
        plt.legend([rtrn_time, dystrn_time, tatrn_time], # plots needed to label
                   handles = [rlgnd,  blgnd, glgnd], # corresponding handle patch colors
                   bbox_to_anchor=(.7, -0.1), #coordinates of the legend
                   ncol=3, #number of columns the legend handles are arranged to
                   borderaxespad=0.) #border between columns
        
        plt.show() # command to show the plot
    # profitability ratios
    def plt_prft_ratios(*in_objs):
        
        ratios_df = fm.multi_period_table(*in_objs)

        # plot color, dimensions, and axes
        plt.style.use(['seaborn-v0_8'])
        plt.figure(figsize=(16,8))
        plt.xlabel('period')
        plt.ylabel('Ratio')
        plt.title('Profitabilty ratios over time')

        # creating lines for each graph, they are assigned to variables for futhur use in 'legend()'
        pm_time = plt.plot(ratios_df.index, ratios_df['Profit Margin'],'ro-')
        ra_time = plt.plot(ratios_df.index, ratios_df['Return on Assets'], 'go-')
        re_time = plt.plot(ratios_df.index, ratios_df['Return on Equity'], 'bo-')
        prev_time = plt.plot(ratios_df.index, ratios_df['Payroll(wages) to Revenue Ratio'], 'co-')

        # assigning patch colors to variables for fithur use in 'legend()'
        rlgnd = mpatches.Patch(color='red', label='Profit Margin')
        blgnd = mpatches.Patch(color='blue', label='Return on Assets')
        glgnd = mpatches.Patch(color='green', label='Return on Equity')
        clgnd = mpatches.Patch(color='cyan', label='Payroll(wages) to Revenue Ratio')
        
        plt.legend([pm_time, ra_time, re_time, prev_time], # plots needed to label
                   handles = [rlgnd,  blgnd, glgnd, clgnd], # corresponding handle patch colors
                   bbox_to_anchor=(.8, -0.1), #coordinates of the legend
                   ncol=4, #number of columns the legend handles are arranged to
                   borderaxespad=0.) #border between columns
        
        plt.show() # command to show the plot
    
    pltin_done = False
    while not pltin_done:    
        try:
            
            ratio_plted = input("""-------------------------------------------------------
            \nFor Liquidity Ratios type: 'liquidity' or 'l', For Financial Leverage Ratios type: 'financial leverage' or 'f'
            \nFor Turnover ratios type: 'turnover' or  't', For Profitability Ratios type: 'profitability' or 'p'
            \nWhich of those ratios do you want to plot?: """) # shows the user the categories for them to choose from
            
            
            lst_stndrd_ans = ['liquidity', 'l', 'financial leverage', 'f', 'turnover' , 't', 'profitability' ,'p']# Assign the standard answer to a list to be used in the next condition 
            if ratio_plted not in lst_stndrd_ans: # executes if the user enters an invalid string answer
                 
                print("""-------------------------------------------------------  
                \nReceived non-standard input input!,
                \nFor Liquidity Ratios type: 'liquidity' or 'l', For Financial Leverage Ratios type: 'financial leverage' or 'f'
                \nFor Turnover ratios type: 'turnover' or  't', For Profitability Ratios type: 'profitability' or 'p'
                """)
                
                continue # restart the prompt above
            
            elif ratio_plted in ['liquidity', 'l']:# user chooses liquidity ratios
                plt_liq_ratios(*in_objs)
            
            elif ratio_plted in ['financial leverage', 'f']:# user chooses financial leverage ratios
                plt_finlev_ratios(*in_objs)
           
            elif ratio_plted in ['turnover' , 't']: # user chooses turnover ratios
                plt_trnvr_ratios(*in_objs)
            
            elif ratio_plted in ['profitability' ,'p']:# user chooses profitability ratios
                plt_prft_ratios(*in_objs)
            # no else statment needed, 
                # if the answer was a string but not standard the if statement caught it,
                # if it was another data type the except clause caught it.
            
            x = False # Does the user want another plot?
            while not x:
                
                ans = str(input('Do you want another plot made? y/n: ')).lower().strip()
                
                # If yes, then break this loop and don't change the value of 'pltin_done'
                if 'y' == ans:
                    x = True
                
                # if no, break the loop and change the value of 'pltin_done' to true to exit the outer loop and end the program
                elif 'n' == ans:
                    x = True
                    pltin_done = True
                
                # executes it the user enters an invalid string answer, here the loop isn't broken, rather it reprompts the user and asks them for a valid answer
                else:
                    print('Non-standard input entered, please say "y" if you want another plot,\n if not please say "n"')

        except ValueError: # executes if there is a problem with the argument entered, the execution for the innerfunctions was interupted
            print('Program Failed to plot your data, possible reasons,\n you entered periods of multiple types of companys\n you entered instances of other classes or no objects at all\n *note that the only valid input to this function is an instance of `cm.company` subclasses')
    
