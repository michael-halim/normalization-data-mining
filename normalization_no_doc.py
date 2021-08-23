""""""""""""""""""""""
No Documentation Code
"""""""""""""""""""""
import pandas as pd
import numpy as np
import math
from statistics import pstdev

def display(col,values):
    new_dict = dict()
    for i in range(len(col)):
        new_dict.update({col[i]:values[i]})

    new_df = pd.DataFrame(data=new_dict)
    print(new_df,end='\n\n')

def main():
    
    sheets = pd.ExcelFile('Latihan Normalisasi.xlsx').sheet_names

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

        for col in df_data.columns:
            cols.append(col)
            data_values.append(df_data[col].tolist())

        min_max, zscore, dscaling = [],[],[]

        for row in data_values:
            tmp_minmax, tmp_zscore, tmp_dscaling = [],[],[]
            row_min, row_max = min(row), max(row)

            AVG = np.mean(row)
            PST_DEV = pstdev(row)

            POWER = math.floor(math.log(row_max,10))
            while row_max/(10**POWER) >= 1:      
                POWER += 1                       

            for num in row:
                tmp_minmax.append((num - row_min) / (row_max - row_min) * (NEW_MAX - NEW_MIN) + NEW_MIN)

                tmp_zscore.append(( num - AVG ) / PST_DEV)

                tmp_dscaling.append(num/(10 ** POWER))

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