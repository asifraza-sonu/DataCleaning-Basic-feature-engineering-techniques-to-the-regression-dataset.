'''#d):Q1'''
import pandas as pd
import numpy as np
import re 
def space_strip(str_data):
    s = (str_data.strip())
    return s
'''#d):Q2'''
dataset = pd.read_csv('final_dataset.csv', delimiter = ',')
my_converter_dict ={'super_area':space_strip,'carpet_area':space_strip}
dataset = pd.read_csv('final_dataset.csv',skiprows = 1,names =[(col.strip().replace(' ','_')) for col in dataset],
                       delimiter = ',',converters =my_converter_dict,skipinitialspace=True,encoding ='utf8')
dataset_in_work=dataset.rename(columns ={'super_area':'square_area'})
dataset_in_work.replace(to_replace='None',value=np.nan,inplace = True)
dataset.replace(to_replace = 'None',value = np.nan,inplace=True)
'''#d):Q3
       Addressed as final step'''
'''#d):Q4'''
feature_matrix_numeric = ['property_price','square_area','carpet_area']
pd.set_option('mode.chained_assignment', None) 
for feature in feature_matrix_numeric:
    i=0
    for s in dataset_in_work[feature].str.strip():
        if str(s)!='nan':
            pp_temp1=re.sub("[,]", "", s)
            pp_temp = re.search(r",?\-?\d+\.?\d*",pp_temp1)
                    
        if feature == 'property_price' and re.search("Cr",s):
            dataset_in_work[feature][i]=round((float(pp_temp.group())*100),4)
            i+=1
        elif feature == 'property_price':
            dataset_in_work[feature][i]=round((float(pp_temp.group())),4)
            i+=1
        elif feature == 'square_area'and str(s)=='nan':            
            dataset_in_work[feature][i]=np.nan
            i+=1
        elif feature == 'square_area' and str(s)!='nan' and re.search("sqft",s):            
            dataset_in_work[feature][i]=round((float(pp_temp.group())),2)
            i+=1
        elif feature == 'square_area' and str(s)!='nan'and re.search("sqm",s):            
            dataset_in_work[feature][i]=round(((float(pp_temp.group()))*10.7639),2)
            i+=1
        elif feature == 'carpet_area'and str(s)=='nan':            
            dataset_in_work[feature][i]=np.nan
            i+=1
        elif feature == 'carpet_area'and str(s)!='nan' and re.search("sqft",s):            
            dataset_in_work[feature][i]=round((float(pp_temp.group())),2)
            i+=1
        elif feature == 'carpet_area' and str(s)!='nan'and re.search("sqyrd",s):            
            dataset_in_work[feature][i]=round(((float(pp_temp.group()))*9),2)
            i+=1

'''#d):Q5'''

mean_property_price= round(dataset_in_work['property_price'].mean(),4)
mean_square_area= round(dataset_in_work['square_area'].mean(),1)
mean_carpet_area = round(dataset_in_work['carpet_area'].mean(),1)

for feature in feature_matrix_numeric:
    for j in range(len(dataset_in_work)):
        k= dataset_in_work.loc[j,feature] 
        if str(k)=='nan':
            if feature == 'property_price':
                dataset_in_work.loc[j,feature]=mean_property_price
            elif feature =='square_area':
                dataset_in_work.loc[j,feature]=mean_square_area
            elif feature =='carpet_area':
                dataset_in_work.loc[j,feature]=mean_carpet_area
    
'''#d):Q6'''       
init_ref_dtypes= dataset.dtypes
feature_matrix_object = ['facing','overlooking','ownership','transaction','furnishing']
feature_matrix_object_cat= ['facing_cat','overlooking_cat','ownership_cat','transaction_cat','furnishing_cat']
dataset_in_work_2 =(dataset_in_work).copy()     
for feature in feature_matrix_object:
    dataset_in_work_2[feature]= dataset_in_work_2[feature].astype('category')
    dataset_in_work_2[feature+'_cat']=dataset_in_work_2[feature].cat.codes
for feature in feature_matrix_object_cat:
    for l in range(len(dataset_in_work_2)):
        if dataset_in_work_2.loc[l,feature]==-1:
            dataset_in_work_2.loc[l,feature]= np.nan
'''#d):Q7'''
for feature in feature_matrix_object_cat:
    for m in range(len(dataset_in_work_2)):
        n= dataset_in_work_2.loc[m,feature] 
        if str(n)=='nan':
            dataset_in_work_2.loc[m,feature]= 0
'''#d):Q8'''
a=0
for s in dataset_in_work_2['floor'].str.strip():
    if str(s)!='nan':
            floor_temp1=re.sub("[,]", "", s)
            floor_temp2=re.sub('Ground','0',floor_temp1)
            floor_temp = re.findall(r",?\-?\d+\.?\d*",floor_temp2)
            for x in range(len(floor_temp)-1):
                floor_temp[x]=float(floor_temp[x])
                floor_temp[x+1]=float(floor_temp[x+1])
                floor_deci= round(floor_temp[x]/floor_temp[x+1],3)
            dataset_in_work_2['floor'][a]=floor_deci
            a+=1
    else:
            floor_temp=np.nan
            floor_deci =np.nan
            dataset_in_work_2['floor'][a]=floor_deci
            a+=1
'''#d):Q9''' 
feature_matrix_fl_bal =['floor','balcony']
dataset_in_work_2.fillna(value={'floor': 0, 'balcony': 0},inplace=True)
'''#d):Q3'''
final_data = dataset_in_work_2.copy()
ref_data = final_data.isna().mean().round(2)*100
dropped_col_data= []
for col in final_data.columns:
    if final_data[col].isna().mean().round(2)*100>40:
        dropped_col_data.append(col)
        final_data= final_data.drop(columns=col,axis =1)
final_data.to_csv('2018AIML551_final_dataset.csv',mode='w', index=False)