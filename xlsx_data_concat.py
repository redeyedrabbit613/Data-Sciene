# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 20:10:20 2024

@author: funky
"""
import glob as gl
import pandas as pd

pattern1 = r'C:\Users\funky\OneDrive\Desktop\Python\Data_Science\cluster_density?.xlsx'
pattern2 = r'C:\Users\funky\OneDrive\Desktop\Python\Data_Science\cluster_density??.xlsx'

file_list = gl.glob(pattern1)
file_list2 = gl.glob(pattern2)
final_list = file_list + file_list2

dfs=[]

for file in final_list:
    df = pd.read_excel(file)
    dfs.append(df)
    
combined_df = pd.concat(dfs, ignore_index=True)

total_raw_spot_count = combined_df['Raw_Spot_Count'].sum()

file_path = r'C:\Users\funky\OneDrive\Desktop\Python\Data_Science\Raw_Spot_Count.xlsx'

total_df = pd.DataFrame({'Total_Raw_Spot_count': [total_raw_spot_count]})
total_df.to_excel(file_path, index = False)

   
    
