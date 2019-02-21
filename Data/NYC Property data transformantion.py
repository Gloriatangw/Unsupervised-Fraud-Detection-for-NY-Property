# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:09:44 2018

@author: alok_
"""

import numpy as np
import pandas as pd
import sklearn as sk
import seaborn as sbrn
import matplotlib.pyplot as plt
import pylab

NYC_Property_data = pd.read_csv('NY property 1 million.csv')

#NYC_Property_data.describe()
#NYC_Property_data.info() 
#NYC_Property_data.head()
#sbrn.heatmap(NYC_Property_data.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#sbrn.heatmap(NYC_Property_data.corr(),annot=False)

NYC_Property_data['LOTAREA'] = NYC_Property_data['LTFRONT'] * NYC_Property_data['LTDEPTH']
NYC_Property_data['BLDAREA'] = NYC_Property_data['BLDFRONT'] * NYC_Property_data['BLDDEPTH']
NYC_Property_data['BLDVOL'] = NYC_Property_data['BLDAREA'] * NYC_Property_data['STORIES']
NYC_Property_data['FULLVAL_per_LOTAREA'] = NYC_Property_data['FULLVAL'] / NYC_Property_data['LOTAREA']
NYC_Property_data['FULLVAL_per_BLDAREA'] = NYC_Property_data['FULLVAL'] / NYC_Property_data['BLDAREA']
NYC_Property_data['FULLVAL_per_BLDVOL'] = NYC_Property_data['FULLVAL'] / NYC_Property_data['BLDVOL']
NYC_Property_data['AVLAND_per_LOTAREA'] = NYC_Property_data['AVLAND'] / NYC_Property_data['LOTAREA']
NYC_Property_data['AVLAND_per_BLDAREA'] = NYC_Property_data['AVLAND'] / NYC_Property_data['BLDAREA']
NYC_Property_data['AVLAND_per_BLDVOL'] = NYC_Property_data['AVLAND'] / NYC_Property_data['BLDVOL']
NYC_Property_data['AVTOT_per_LOTAREA'] = NYC_Property_data['AVTOT'] / NYC_Property_data['LOTAREA']
NYC_Property_data['AVTOT_per_BLDAREA'] = NYC_Property_data['AVTOT'] / NYC_Property_data['BLDAREA']
NYC_Property_data['AVTOT_per_BLDVOL'] = NYC_Property_data['AVTOT'] / NYC_Property_data['BLDVOL']

NYC_Property_data.replace([np.inf, -np.inf], 0,inplace=True)
    
ZIP5_AVG_FULLVAL_per_LOTAREA = NYC_Property_data.groupby('ZIP5',axis=0).mean()['FULLVAL_per_LOTAREA'].reset_index()
ZIP5_AVG_FULLVAL_per_LOTAREA.rename(columns = {'FULLVAL_per_LOTAREA':'FULLVAL_per_LOTAREA_AVG_ZIP5'}, inplace = True)
ZIP5_AVG_FULLVAL_per_BLDAREA = NYC_Property_data.groupby('ZIP5',axis=0).mean()['FULLVAL_per_BLDAREA'].reset_index()
ZIP5_AVG_FULLVAL_per_BLDAREA.rename(columns = {'FULLVAL_per_BLDAREA':'FULLVAL_per_BLDAREA_ACG_ZIP5'}, inplace = True)
ZIP5_AVG_FULLVAL_per_BLDVOL = NYC_Property_data.groupby('ZIP5',axis=0).mean()['FULLVAL_per_BLDVOL'].reset_index()
ZIP5_AVG_FULLVAL_per_BLDVOL.rename(columns = {'FULLVAL_per_BLDVOL':'FULLVAL_per_BLDVOL_AVG_ZIP5'}, inplace = True)
ZIP5_AVG_AVLAND_per_LOTAREA = NYC_Property_data.groupby('ZIP5',axis=0).mean()['AVLAND_per_LOTAREA'].reset_index()
ZIP5_AVG_AVLAND_per_LOTAREA.rename(columns = {'AVLAND_per_LOTAREA':'AVLAND_per_LOTAREA_AVG_ZIP5'}, inplace = True)
ZIP5_AVG_AVLAND_per_BLDAREA = NYC_Property_data.groupby('ZIP5',axis=0).mean()['AVLAND_per_BLDAREA'].reset_index()
ZIP5_AVG_AVLAND_per_BLDAREA.rename(columns = {'AVLAND_per_BLDAREA':'AVLAND_per_BLDAREA_AVG_ZIP5'}, inplace = True)
ZIP5_AVG_AVLAND_per_BLDVOL = NYC_Property_data.groupby('ZIP5',axis=0).mean()['AVLAND_per_BLDVOL'].reset_index()
ZIP5_AVG_AVLAND_per_BLDVOL.rename(columns = {'AVLAND_per_BLDVOL':'AVLAND_per_BLDVOL_ZIP5'}, inplace = True)
ZIP5_AVG_AVTOT_per_LOTAREA = NYC_Property_data.groupby('ZIP5',axis=0).mean()['AVTOT_per_LOTAREA'].reset_index()
ZIP5_AVG_AVTOT_per_LOTAREA.rename(columns = {'AVTOT_per_LOTAREA':'AVTOT_per_LOTAREA_ZIP5'}, inplace = True)
ZIP5_AVG_AVTOT_per_BLDAREA = NYC_Property_data.groupby('ZIP5',axis=0).mean()['AVTOT_per_BLDAREA'].reset_index()
ZIP5_AVG_AVTOT_per_BLDAREA.rename(columns = {'AVTOT_per_BLDAREA':'AVTOT_per_BLDAREA_ZIP5'}, inplace = True)
ZIP5_AVG_AVTOT_per_BLDVOL = NYC_Property_data.groupby('ZIP5',axis=0).mean()['AVTOT_per_BLDVOL'].reset_index()
ZIP5_AVG_AVTOT_per_BLDVOL.rename(columns = {'AVTOT_per_BLDVOL':'AVTOT_per_BLDVOL_AVG_ZIP5'}, inplace = True)


ZIP3_AVG_FULLVAL_per_LOTAREA = NYC_Property_data.groupby('ZIP3',axis=0).mean()['FULLVAL_per_LOTAREA'].reset_index()
ZIP3_AVG_FULLVAL_per_LOTAREA.rename(columns = {'FULLVAL_per_LOTAREA':'FULLVAL_per_LOTAREA_AVG_ZIP3'}, inplace = True)
ZIP3_AVG_FULLVAL_per_BLDAREA = NYC_Property_data.groupby('ZIP3',axis=0).mean()['FULLVAL_per_BLDAREA'].reset_index()
ZIP3_AVG_FULLVAL_per_BLDAREA.rename(columns = {'FULLVAL_per_BLDAREA':'FULLVAL_per_BLDAREA_ACG_ZIP3'}, inplace = True)
ZIP3_AVG_FULLVAL_per_BLDVOL = NYC_Property_data.groupby('ZIP3',axis=0).mean()['FULLVAL_per_BLDVOL'].reset_index()
ZIP3_AVG_FULLVAL_per_BLDVOL.rename(columns = {'FULLVAL_per_BLDVOL':'FULLVAL_per_BLDVOL_AVG_ZIP3'}, inplace = True)
ZIP3_AVG_AVLAND_per_LOTAREA = NYC_Property_data.groupby('ZIP3',axis=0).mean()['AVLAND_per_LOTAREA'].reset_index()
ZIP3_AVG_AVLAND_per_LOTAREA.rename(columns = {'AVLAND_per_LOTAREA':'AVLAND_per_LOTAREA_AVG_ZIP3'}, inplace = True)
ZIP3_AVG_AVLAND_per_BLDAREA = NYC_Property_data.groupby('ZIP3',axis=0).mean()['AVLAND_per_BLDAREA'].reset_index()
ZIP3_AVG_AVLAND_per_BLDAREA.rename(columns = {'AVLAND_per_BLDAREA':'AVLAND_per_BLDAREA_AVG_ZIP3'}, inplace = True)
ZIP3_AVG_AVLAND_per_BLDVOL = NYC_Property_data.groupby('ZIP3',axis=0).mean()['AVLAND_per_BLDVOL'].reset_index()
ZIP3_AVG_AVLAND_per_BLDVOL.rename(columns = {'AVLAND_per_BLDVOL':'AVLAND_per_BLDVOL_ZIP3'}, inplace = True)
ZIP3_AVG_AVTOT_per_LOTAREA = NYC_Property_data.groupby('ZIP3',axis=0).mean()['AVTOT_per_LOTAREA'].reset_index()
ZIP3_AVG_AVTOT_per_LOTAREA.rename(columns = {'AVTOT_per_LOTAREA':'AVTOT_per_LOTAREA_ZIP3'}, inplace = True)
ZIP3_AVG_AVTOT_per_BLDAREA = NYC_Property_data.groupby('ZIP3',axis=0).mean()['AVTOT_per_BLDAREA'].reset_index()
ZIP3_AVG_AVTOT_per_BLDAREA.rename(columns = {'AVTOT_per_BLDAREA':'AVTOT_per_BLDAREA_ZIP3'}, inplace = True)
ZIP3_AVG_AVTOT_per_BLDVOL = NYC_Property_data.groupby('ZIP3',axis=0).mean()['AVTOT_per_BLDVOL'].reset_index()
ZIP3_AVG_AVTOT_per_BLDVOL.rename(columns = {'AVTOT_per_BLDVOL':'AVTOT_per_BLDVOL_AVG_ZIP3'}, inplace = True)



TAXCLASS_AVG_FULLVAL_per_LOTAREA = NYC_Property_data.groupby('TAXCLASS',axis=0).mean()['FULLVAL_per_LOTAREA'].reset_index()
TAXCLASS_AVG_FULLVAL_per_LOTAREA.rename(columns = {'FULLVAL_per_LOTAREA':'FULLVAL_per_LOTAREA_AVG_TAX'}, inplace = True)
TAXCLASS_AVG_FULLVAL_per_BLDAREA = NYC_Property_data.groupby('TAXCLASS',axis=0).mean()['FULLVAL_per_BLDAREA'].reset_index()
TAXCLASS_AVG_FULLVAL_per_BLDAREA.rename(columns = {'FULLVAL_per_BLDAREA':'FULLVAL_per_BLDAREA_AVG_TAX'}, inplace = True)
TAXCLASS_AVG_FULLVAL_per_BLDVOL = NYC_Property_data.groupby('TAXCLASS',axis=0).mean()['FULLVAL_per_BLDVOL'].reset_index()
TAXCLASS_AVG_FULLVAL_per_BLDVOL.rename(columns = {'FULLVAL_per_BLDVOL':'FULLVAL_per_BLDVOL_AVG_TAX'}, inplace = True)
TAXCLASS_AVG_AVLAND_per_LOTAREA = NYC_Property_data.groupby('TAXCLASS',axis=0).mean()['AVLAND_per_LOTAREA'].reset_index()
TAXCLASS_AVG_AVLAND_per_LOTAREA.rename(columns = {'AVLAND_per_LOTAREA':'AVLAND_per_LOTAREA_AVG_TAX'}, inplace = True)
TAXCLASS_AVG_AVLAND_per_BLDAREA = NYC_Property_data.groupby('TAXCLASS',axis=0).mean()['AVLAND_per_BLDAREA'].reset_index()
TAXCLASS_AVG_AVLAND_per_BLDAREA.rename(columns = {'AVLAND_per_BLDAREA':'AVLAND_per_BLDAREA_AVG_TAX'}, inplace = True)
TAXCLASS_AVG_AVLAND_per_BLDVOL = NYC_Property_data.groupby('TAXCLASS',axis=0).mean()['AVLAND_per_BLDVOL'].reset_index()
TAXCLASS_AVG_AVLAND_per_BLDVOL.rename(columns = {'AVLAND_per_BLDVOL':'AVLAND_per_BLDVOL_AVG_TAX'}, inplace = True)
TAXCLASS_AVG_AVTOT_per_LOTAREA = NYC_Property_data.groupby('TAXCLASS',axis=0).mean()['AVTOT_per_LOTAREA'].reset_index()
TAXCLASS_AVG_AVTOT_per_LOTAREA.rename(columns = {'AVTOT_per_LOTAREA':'AVTOT_per_LOTAREA_AVG_TAX'}, inplace = True)
TAXCLASS_AVG_AVTOT_per_BLDAREA = NYC_Property_data.groupby('TAXCLASS',axis=0).mean()['AVTOT_per_BLDAREA'].reset_index()
TAXCLASS_AVG_AVTOT_per_BLDAREA.rename(columns = {'AVTOT_per_BLDAREA':'AVTOT_per_BLDAREA_AVG_TAX'}, inplace = True)
TAXCLASS_AVG_AVTOT_per_BLDVOL = NYC_Property_data.groupby('TAXCLASS',axis=0).mean()['AVTOT_per_BLDVOL'].reset_index()
TAXCLASS_AVG_AVTOT_per_BLDVOL.rename(columns = {'AVTOT_per_BLDVOL':'AVTOT_per_BLDVOL_AVG_TAX'}, inplace = True)



BLOCK_AVG_FULLVAL_per_LOTAREA = NYC_Property_data.groupby('BLOCK',axis=0).mean()['FULLVAL_per_LOTAREA'].reset_index()
BLOCK_AVG_FULLVAL_per_LOTAREA.rename(columns = {'FULLVAL_per_LOTAREA':'FULLVAL_per_LOTAREA_AVG_BLK'}, inplace = True)
BLOCK_AVG_FULLVAL_per_BLDAREA = NYC_Property_data.groupby('BLOCK',axis=0).mean()['FULLVAL_per_BLDAREA'].reset_index()
BLOCK_AVG_FULLVAL_per_BLDAREA.rename(columns = {'FULLVAL_per_BLDAREA':'FULLVAL_per_BLDAREA_AVG_BLK'}, inplace = True)
BLOCK_AVG_FULLVAL_per_BLDVOL = NYC_Property_data.groupby('BLOCK',axis=0).mean()['FULLVAL_per_BLDVOL'].reset_index()
BLOCK_AVG_FULLVAL_per_BLDVOL.rename(columns = {'FULLVAL_per_BLDVOL':'FULLVAL_per_BLDVOL_AVG_BLK'}, inplace = True)
BLOCK_AVG_AVLAND_per_LOTAREA = NYC_Property_data.groupby('BLOCK',axis=0).mean()['AVLAND_per_LOTAREA'].reset_index()
BLOCK_AVG_AVLAND_per_LOTAREA.rename(columns = {'AVLAND_per_LOTAREA':'AVLAND_per_LOTAREA_AVG_BLK'}, inplace = True)
BLOCK_AVG_AVLAND_per_BLDAREA = NYC_Property_data.groupby('BLOCK',axis=0).mean()['AVLAND_per_BLDAREA'].reset_index()
BLOCK_AVG_AVLAND_per_BLDAREA.rename(columns = {'AVLAND_per_BLDAREA':'AVLAND_per_BLDAREA_AVG_BLK'}, inplace = True)
BLOCK_AVG_AVLAND_per_BLDVOL = NYC_Property_data.groupby('BLOCK',axis=0).mean()['AVLAND_per_BLDVOL'].reset_index()
BLOCK_AVG_AVLAND_per_BLDVOL.rename(columns = {'AVLAND_per_BLDVOL':'AVLAND_per_BLDVOL_AVG_BLK'}, inplace = True)
BLOCK_AVG_AVTOT_per_LOTAREA = NYC_Property_data.groupby('BLOCK',axis=0).mean()['AVTOT_per_LOTAREA'].reset_index()
BLOCK_AVG_AVTOT_per_LOTAREA.rename(columns = {'AVTOT_per_LOTAREA':'AVTOT_per_LOTAREA_AVG_BLK'}, inplace = True)
BLOCK_AVG_AVTOT_per_BLDAREA = NYC_Property_data.groupby('BLOCK',axis=0).mean()['AVTOT_per_BLDAREA'].reset_index()
BLOCK_AVG_AVTOT_per_BLDAREA.rename(columns = {'AVTOT_per_BLDAREA':'AVTOT_per_BLDAREA_AVG_BLK'}, inplace = True)
BLOCK_AVG_AVTOT_per_BLDVOL = NYC_Property_data.groupby('BLOCK',axis=0).mean()['AVTOT_per_BLDVOL'].reset_index()
BLOCK_AVG_AVTOT_per_BLDVOL.rename(columns = {'AVTOT_per_BLDVOL':'AVTOT_per_BLDVOL_AVG_BLK'}, inplace = True)




NYC_Property_data = NYC_Property_data.merge(ZIP5_AVG_FULLVAL_per_LOTAREA, on='ZIP5', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP5_AVG_FULLVAL_per_BLDAREA, on='ZIP5', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP5_AVG_FULLVAL_per_BLDVOL, on='ZIP5', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP5_AVG_AVLAND_per_LOTAREA, on='ZIP5', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP5_AVG_AVLAND_per_BLDAREA, on='ZIP5', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP5_AVG_AVLAND_per_BLDVOL, on='ZIP5', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP5_AVG_AVTOT_per_LOTAREA, on='ZIP5', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP5_AVG_AVTOT_per_BLDAREA, on='ZIP5', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP5_AVG_AVTOT_per_BLDVOL, on='ZIP5', how='left')

NYC_Property_data = NYC_Property_data.merge(ZIP3_AVG_FULLVAL_per_LOTAREA, on='ZIP3', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP3_AVG_FULLVAL_per_BLDAREA, on='ZIP3', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP3_AVG_FULLVAL_per_BLDVOL, on='ZIP3', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP3_AVG_AVLAND_per_LOTAREA, on='ZIP3', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP3_AVG_AVLAND_per_BLDAREA, on='ZIP3', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP3_AVG_AVLAND_per_BLDVOL, on='ZIP3', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP3_AVG_AVTOT_per_LOTAREA, on='ZIP3', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP3_AVG_AVTOT_per_BLDAREA, on='ZIP3', how='left')
NYC_Property_data = NYC_Property_data.merge(ZIP3_AVG_AVTOT_per_BLDVOL, on='ZIP3', how='left')


NYC_Property_data = NYC_Property_data.merge(TAXCLASS_AVG_FULLVAL_per_LOTAREA, on='TAXCLASS', how='left')
NYC_Property_data = NYC_Property_data.merge(TAXCLASS_AVG_FULLVAL_per_BLDAREA, on='TAXCLASS', how='left')
NYC_Property_data = NYC_Property_data.merge(TAXCLASS_AVG_FULLVAL_per_BLDVOL, on='TAXCLASS', how='left')
NYC_Property_data = NYC_Property_data.merge(TAXCLASS_AVG_AVLAND_per_LOTAREA, on='TAXCLASS', how='left')
NYC_Property_data = NYC_Property_data.merge(TAXCLASS_AVG_AVLAND_per_BLDAREA, on='TAXCLASS', how='left')
NYC_Property_data = NYC_Property_data.merge(TAXCLASS_AVG_AVLAND_per_BLDVOL, on='TAXCLASS', how='left')
NYC_Property_data = NYC_Property_data.merge(TAXCLASS_AVG_AVTOT_per_LOTAREA, on='TAXCLASS', how='left')
NYC_Property_data = NYC_Property_data.merge(TAXCLASS_AVG_AVTOT_per_BLDAREA, on='TAXCLASS', how='left')
NYC_Property_data = NYC_Property_data.merge(TAXCLASS_AVG_AVTOT_per_BLDVOL, on='TAXCLASS', how='left')

NYC_Property_data = NYC_Property_data.merge(BLOCK_AVG_FULLVAL_per_LOTAREA, on='BLOCK', how='left')
NYC_Property_data = NYC_Property_data.merge(BLOCK_AVG_FULLVAL_per_BLDAREA, on='BLOCK', how='left')
NYC_Property_data = NYC_Property_data.merge(BLOCK_AVG_FULLVAL_per_BLDVOL, on='BLOCK', how='left')
NYC_Property_data = NYC_Property_data.merge(BLOCK_AVG_AVLAND_per_LOTAREA, on='BLOCK', how='left')
NYC_Property_data = NYC_Property_data.merge(BLOCK_AVG_AVLAND_per_BLDAREA, on='BLOCK', how='left')
NYC_Property_data = NYC_Property_data.merge(BLOCK_AVG_AVLAND_per_BLDVOL, on='BLOCK', how='left')
NYC_Property_data = NYC_Property_data.merge(BLOCK_AVG_AVTOT_per_LOTAREA, on='BLOCK', how='left')
NYC_Property_data = NYC_Property_data.merge(BLOCK_AVG_AVTOT_per_BLDAREA, on='BLOCK', how='left')
NYC_Property_data = NYC_Property_data.merge(BLOCK_AVG_AVTOT_per_BLDVOL, on='BLOCK', how='left')

NYC_Property_data.columns

NYC_Property_data.head()

NYC_Property_data.to_csv('NY_property_1_million_var_transformed.csv', encoding='utf-8')

