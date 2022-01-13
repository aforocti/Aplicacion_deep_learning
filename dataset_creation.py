import re
import pandas as pd
import csv
import datetime

def getOnlyUsername(word):
    if "\\" in word:
        username = word.split("\\")[1]
    elif "@" in word:
        username = word.split("@")[0]
    else: 
        username = word
    return username

reportFile = "report.txt"
report2File = "report2.txt"
#csvFile = "dataset_with_NA.csv"
csvFile = "dataset_usernames_corrected.csv"

txt1 = "----------------- ---------------- ------------- ------------------"
txt2 = "MAC Address       AP Name          Status        Username                        "
txt3 = ""
txt4 = " "
txt5 = "Disassociated"

f = open(reportFile)
f2 = open(report2File)
dataset = []

for line in f.readlines() + f2.readlines():
    spt = line.strip().split(",")
    if txt1 in spt:
        spt.remove(txt1)
    if txt2 in spt:
        spt.remove(txt2)
    if txt3 in spt:
        spt.remove(txt3)
    if txt4 in spt:
        spt.remove(txt4)   

    #Eliminar espacio en archivo. 26.10.2021
    dateTime = date_time_obj = datetime.datetime.strptime(spt[0]+" "+spt[1], '%d/%m/%Y %H:%M:%S')

    for client in spt[2:]:
        if txt5 in client:
            ind = client.index(txt5)
            client = client[:ind+13] + " " + client[ind+13:]
        client = client.strip()
        client = re.sub(r"\s+"," ",client)
        data = client.split(" ")
        mac_address = data[0]
        ap = data[1]
        if(len(data)<4):
            username = "N/A"
        else:
            username = data[3]
            username = getOnlyUsername(username)

        #For creation with N/A
        #dataset.append([date,hour,username,mac_address,ap]) 
        if(username != "N/A"):
            dataset.append([dateTime,username,mac_address,ap])

f.close()
f2.close()
dataframe = pd.DataFrame(dataset)
dataframe.columns = ["DateTime","Username","MacAddress","AccessPoint"]
dataframe = dataframe.sort_values(by='DateTime')
dataframe.to_csv(csvFile, index=False)
print(dataframe)
print(dataframe.groupby("Username")["Username"].count())