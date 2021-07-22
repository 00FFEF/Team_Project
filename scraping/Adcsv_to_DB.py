
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Team_Project.settings")
#
# import django
# django.setup()
#
# import pandas as pd
# import csv
# from dbapp.models import Admachine
#
# with open('C:\\Develops\\Team_Project\\files\\Social_Network_Ads.csv','r') as f:
#     dr = csv.DictReader(f)
#     s = pd.DataFrame(dr)
# ss = []
# for i in range(len(s)):
#     st = (s['User ID'][i], s['Gender'][i], s['Age'][i], s['EstimatedSalary'][i], s['Purchased'][i])
#     ss.append(st)
# for i in range(len(s)):
#     Admachine.objects.create(UserID=ss[i][0],Gender=ss[i][1],Age=ss[i][2],EstimatedSalary=ss[i][3],Purchased=ss[i][4])
import sqlite3
connect = sqlite3.connect('../db.sqlite3')
cursor = connect.cursor()
import pandas as pd

df = pd.read_csv('C:\\Develops\\Team_Project\\files\\Social_Network_Ads.csv')

for i in range(len(df)):
    UserID = str(df['User ID'][i])
    Gender = df['Gender'][i]
    Age = str(df['Age'][i])
    EstimatedSalary = str(df['EstimatedSalary'][i])
    Purchased = str(df['Purchased'][i])

    try:
        cursor.execute(
            "insert into dbapp_admachine(UserID, Gender, Age, EstimatedSalary, Purchased) values(?,?,?,?,?)", (UserID,Gender,Age,EstimatedSalary,Purchased))
        print(UserID, " | ",Gender, " | ", Age, " | ",EstimatedSalary, " | ", Purchased)
    except:
        pass

connect.commit()
connect.close()