import numpy as np
import pandas as pd
import plotly.express as px
import datetime
df=pd.read_csv(r"C:\Users\Lakshya\Downloads\corona\IndividualDetails.csv")

df.dropna(subset=["current_status"],inplace=True)
Total_cases=df["current_status"].shape[0]

Recovered_cases=df[df["current_status"]=="Recovered"].shape[0]
Death_cases=df[df["current_status"]=="Deceased"].shape[0]
Active_cases=df[df["current_status"]=="Hospitalized"].shape[0]
cases=pd.read_csv("C:\\Users\\Lakshya\\Downloads\\corona\\covid_19_india.csv")
cases["Date"]=pd.to_datetime(cases["Date"])

# a=cases.groupby("Date").sum()["Confirmed"].reset_index()
# a=a.sort_values("Date")
# fig=px.line(a,x="Date",y="Confirmed",title="Day by Day Analysis",labels={"Date":"Date","Confirmed":"Total Cases"})
# fig.update_xaxes(nticks=50)
# fig.show()
# pbar=df["detected_state"].value_counts().reset_index()
# print(pbar)
age= pd.read_csv(r"C:\Users\Lakshya\Downloads\corona\AgeGroupDetails.csv")
px.pie(age,x="AgeGroup",y="TotalCases",title="Age Distribution",annot=True)