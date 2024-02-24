# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 19:52:35 2024

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

final_df = pd.concat(dfs, ignore_index=True)

final_df_file_path = r'C:\Users\funky\OneDrive\Desktop\Python\Data_Science\cluster_density_final.xlsx'
final_df.to_excel(final_df_file_path, index = False)
print(f"Combined data saved to '{final_df_file_path}'")