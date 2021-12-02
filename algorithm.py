import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from apyori import apriori
import datetime

from sklearn.preprocessing import LabelEncoder

def dataframeRules(lista):
    dataset = []
    for item in lista:
        pair = item[0]
        items = [x for x in pair]
        if(":" in items[0] ):
            dataset.append([items[0],items[1],item[1],item[2][0][2],item[2][0][3]])
        else:
            dataset.append([items[1],items[0],item[1],item[2][0][2],item[2][0][3]])
    return pd.DataFrame(dataset,columns=["A","B","Support","Confidence","Lift"])






dataframe = pd.read_csv("dataset.csv")

dataframe['DateTime']= pd.to_datetime(dataframe['DateTime'])

print("****Dataframe CSV***")
dataframe.head()   

print("****GrouBy Usernames***")
dataframegb = dataframe.groupby("Username")["Username"].hist(figsize=(20,8),xlabelsize=8)
print(dataframegb)

print("****Group by datetime****")
df = dataframe.groupby([dataframe['DateTime'].dt.date]).mean()["DateTime"]
print(df)


#Section of dataframe
date_start = datetime.datetime.strptime("17/10/2021 00:00:00", '%d/%m/%Y %H:%M:%S')
date_end = datetime.datetime.strptime("21/10/2021 00:00:00", '%d/%m/%Y %H:%M:%S')
df_section1 = dataframe[(dataframe['DateTime'] > date_start) & (dataframe['DateTime'] < date_end)]
df_section1


#Section 2 of dataframe
date_start = datetime.datetime.strptime("11/11/2021 00:00:00", '%d/%m/%Y %H:%M:%S')
date_end = datetime.datetime.strptime("17/11/2021 00:00:00", '%d/%m/%Y %H:%M:%S')
df_section2 = dataframe[(dataframe['DateTime'] > date_start) & (dataframe['DateTime'] < date_end)]
df_section2


#Total records
df_records_total = dataframe.drop(columns=['DateTime','Access_Point'])
records_total = df_records_total.to_records(index=False)

#Section 1 records
df_records_section1 = df_section1.drop(columns=['DateTime','Access_Point'])
record_section1 = df_records_section1.to_records(index=False)


association_rules_total = apriori(records_total, min_support=0.0045,min_confidence=0.2,min_lift=3,min_length=2)
association_results_total = list(association_rules_total)
dataframe_rules_total = dataframeRules(association_results_total)
print("**** Rules Dataframe Total ****")
print(dataframe_rules_total.head())

association_rules_section1 = apriori(record_section1, min_support=0.0045,min_confidence=0.2,min_lift=3,min_length=2)
association_results_section1 = list(association_rules_section1)
dataframe_rules_section1 = dataframeRules(association_results_section1)
print("**** Rules Dataframe Section 1 ****")
print(dataframe_rules_section1.head())

#Difference from sections
a = pd.concat([dataframe_rules_total.drop(columns=["Support","Confidence","Lift"]), dataframe_rules_section1.drop(columns=["Support","Confidence","Lift"])]).drop_duplicates(keep=False)
print(a)

print(a.groupby(by=["A"]).sum())
