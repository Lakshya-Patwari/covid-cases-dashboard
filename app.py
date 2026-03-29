import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

external_stylesheets = [
    {
        'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB',
        'crossorigin': 'anonymous'
    }
]
df=pd.read_csv(r"C:\Users\Lakshya\Downloads\corona\IndividualDetails.csv")

df.dropna(subset=["current_status"],inplace=True)
Total_cases=df["current_status"].shape[0]

Recovered_cases=df[df["current_status"]=="Recovered"].shape[0]
Death_cases=df[df["current_status"]=="Deceased"].shape[0]
Active_cases=df[df["current_status"]=="Hospitalized"].shape[0]

options = [
    {"label": "All", "value": "All"},
    {"label": "Active", "value": "Hospitalized"},
    {"label": "Recovered", "value": "Recovered"},
    {"label": "Deaths", "value": "Deceased"},
]
cases=pd.read_csv("C:\\Users\\Lakshya\\Downloads\\corona\\covid_19_india.csv")
cases["Date"]=pd.to_datetime(cases["Date"])

a=cases.groupby("Date").sum()["Confirmed"].reset_index()
a=a.sort_values("Date")
fig=px.line(a,x="Date",y="Confirmed",title="Day by Day Analysis",labels={"Date":"Date","Confirmed":"Total Cases"})
fig.update_xaxes(nticks=30)
age= pd.read_csv(r"C:\Users\Lakshya\Downloads\corona\AgeGroupDetails.csv")
fig2=px.pie(age,names="AgeGroup",values="TotalCases",title="Age Distribution")


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout=html.Div([
    html.H1("Corona Virus Pandemic",style={"textAlign":"center"}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases"),
                    html.H4(Total_cases)
                    ],className="card-body")
                ],className="card bg-danger ")],className ="col-md-3"),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases"),
                    html.H4(Active_cases)
                    ],className="card-body")
                ],className="card bg-info")
            ],className ="col-md-3"),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Cases"),
                    html.H4(Recovered_cases)
                    ],className="card-body")
                ],className="card bg-warning ")],className ="col-md-3"),
        html.Div([html.Div([
                html.Div([
                    html.H3("Total Deaths"),
                    html.H4(Death_cases)
                    ],className="card-body")
                ],className="card bg-success")
            ],className ="col-md-3")
    ],className="row"),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(id="line",figure=fig)
                ],className="card-body")
                
            ],className="card")
        ],className ="col-md-6"),
        html.Div([
            html.Div([
                html.Div([
                    dcc.Graph(id="pie",figure=fig2)
                ],className="card-body")
                
            ],className="card")
        ],className ="col-md-6")
        
        
        
    ],className="row"),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id="picker",options=options,value="All"),
                    dcc.Graph(id="bar")
                ],className="card-body")
            ],className="card")
        ],className="col-md-12")
    ],className="row")
],className ="container")

@app.callback(Output("bar","figure"),[Input("picker","value")])
def update_graph(type):
    if type =="All":
        pbar=df["detected_state"].value_counts().reset_index()
    else:
        npat=df[df["current_status"]==type]
        pbar=npat["detected_state"].value_counts().reset_index()
    
    fig = px.bar(pbar, x="detected_state", y="count", title="Total State Count")
    return fig

if __name__ =="__main__":
    app.run(debug = True)