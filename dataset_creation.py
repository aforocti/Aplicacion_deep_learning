import re
import pandas as pd
import csv

reportFile = "report.txt"
csvFile = "dataset.csv"

txt1 = "----------------- ---------------- ------------- ------------------"
txt2 = "MAC Address       AP Name          Status        Username                        "
txt3 = ""
txt4 = " "

f = open(reportFile)
dataset = []

for line in f.readlines():
    spt = line.strip().split(",")
    if txt1 in spt:
        spt.remove(txt1)
    if txt2 in spt:
        spt.remove(txt2)
    if txt3 in spt:
        spt.remove(txt3)
    if txt4 in spt:
        spt.remove(txt4)
    date = spt[0]
    hour = spt[1]
    for client in spt[2:]:
        client = client.strip()
        client = re.sub(r"\s+"," ",client)
        data = client.split(" ")
        mac_address = data[0]
        ap = data[1]
        username = data[3]
        dataset.append([date,hour,username,mac_address,ap])

f.close()
dataframe = pd.DataFrame(dataset)
dataframe.columns = ["Date","Time","Username","Mac Address","Access Point"]
dataframe.to_csv(csvFile, index=False)
print(dataframe)
print(dataframe.groupby("Username")["Username"].count())