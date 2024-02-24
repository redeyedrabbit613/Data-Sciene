# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 20:33:38 2024

@author: funky
"""

import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

current = 0

def new_df():
    global current
    current += 1
    df = pd.DataFrame(np.random.randint(0,10,(10,5)), columns = 'FCID Lane Swath Read Raw_Spot_Count'.split())
    print(df) 
    file_path = f'C:/Users/funky/OneDrive/Desktop/Python/Data_Science/cluster_density{current}.xlsx'
    df.to_excel(file_path, index=False)
    print(f"DataFrame save to '{file_path}'")
    
counter = 0 
while counter <10:
    new_df()
    counter +=1
    
    