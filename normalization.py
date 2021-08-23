"""
Why Nomarlized ? 
Because data in database can be processed faster if the numbers are small

Min Max Normalization

v' = ( v - old_minimum ) / (old_maximum - old_minimum) * (new_max - new_min) + new_min
**Notes
v' = new number
v  = old number
old_maximum = maximum number from one column
old_minimum = minimum number from one column

Z Score Nomarlization
v' = (v - old_average ) / old std_dev
**Notes
old_average = average from one column
std_dev = std dev (population) from one column

Normalization by decimal scaling
v' =  v / ( 10^j )
where j is the smallest integer such that Max|v'| < 1
"""
import pandas as pd
import numpy as np
import math
from statistics import pstdev #to get std dev population function

def display(col,values):
    new_dict = dict()
    for i in range(len(col)):
        new_dict.update({col[i]:values[i]})

    new_df = pd.DataFrame(data=new_dict)
    print(new_df,end='\n\n')

def main():
    
    sheets = pd.ExcelFile('Latihan Normalisasi.xlsx').sheet_names       # Get all Worksheets name in the file

    START_INDEX = 0
    END_INDEX = 2

    print('SHEET(S) THAT WILL BE CALCULATED')
    print(sheets[START_INDEX:END_INDEX],end='\n\n')

    for sheet in sheets[START_INDEX : END_INDEX]:
        print('=========================================================')
        df_data = pd.read_excel('Latihan Normalisasi.xlsx',sheet_name = sheet)
        print('INITIAL DATA')
        print(df_data,end='\n\n')

        NEW_MAX = 1
        NEW_MIN = 0

        cols , data_values = [],[]

        for col in df_data.columns:                         # get every values fro every column and 
            cols.append(col)                                # put it in list
            data_values.append(df_data[col].tolist())

        min_max, zscore, dscaling = [],[],[]

        for row in data_values:
            tmp_minmax, tmp_zscore, tmp_dscaling = [],[],[]
            row_min, row_max = min(row), max(row)           # get Min and Max

            AVG = np.mean(row)                              # get Average
            PST_DEV = pstdev(row)                           # get Std Dev for Population

            POWER = math.floor(math.log(row_max,10))
            while row_max/(10**POWER) >= 1:                 # There's no definitive formula i found that exactly get the power
                POWER += 1                                  # so i add one by one after the log for the exact power

            for num in row:
                tmp_minmax.append((num - row_min) / (row_max - row_min) * (NEW_MAX - NEW_MIN) + NEW_MIN) # Min Max Normalization

                tmp_zscore.append(( num - AVG ) / PST_DEV)        # Z Score Normalization

                tmp_dscaling.append(num/(10 ** POWER))            # Decimal Scaling Normalization

            min_max.append(tmp_minmax)
            zscore.append(tmp_zscore)
            dscaling.append(tmp_dscaling)

        print('MIN MAX NORMALIZATION')
        display(cols,min_max)

        print('Z SCORE NOMARLIZATION')
        display(cols,zscore)

        print('DECIMAL SCALING NORMALIZATION') 
        display(cols,dscaling)

if __name__ == '__main__':
    main()