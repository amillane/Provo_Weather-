from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output
import pandas as pd


df = pd.read_csv('weather.csv')#, index_col = 'datetime', parse_dates = True)
df.drop(df.columns[[0]],axis = 1, inplace = True)

app = Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="multi",
        row_deletable=True,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 10,
    ),
    html.Div(id='datatable-interactivity-container')
])

@app.callback(
    Output('datatable-interactivity', 'style_data_conditional'),
    Input('datatable-interactivity', 'selected_columns'))

def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'} for i in selected_columns]


