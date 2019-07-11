# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
# from dash.dependencies import Input, Output
#
# import plotly.plotly as py
# import plotly.graph_objs as go
#
# import pandas as pd
# import numpy as np
# from datetime import datetime
# import pandas_datareader.data as web

# test imports
# import json

external_css = [
    # dash stylesheet
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css',
    'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'
]


# Parameters


'''
Build the App
'''
app = dash.Dash()
# app = dash.Dash(url_base_pathname='/police/')
server = app.server

# used when assigning callbacks to components that are generated by other callbacks (and therefore not in the initial layout), then you can suppress this exception by setting
app.config['suppress_callback_exceptions']=True

# if your app is served under /my-proxy/ but your proxy server removes the /my-proxy/ prefix before forwarding the request to the underlying dash server, you can set
# app.config.update({
#     'routes_pathname_prefix': '/',

#     'requests_pathname_prefix': 'police/'
# })

app.layout = html.Div(children=[

    dcc.Markdown('''
        # San Fran Police Reports
        This data includes incidents from the San Francisco Police Department (SFPD) Crime Incident Reporting system, from January 2003 until the present (2 weeks ago from current date). The dataset is updated daily.
        Documentation on the data: [San Francisco Police data](https://cloud.google.com/bigquery/public-data/sfpd-reports).

        > This app demonstrates both the us of Google's BigQuery API to handle large volumes of data and Folium a python library based on Leaflet.js for creating stunning maps.

        ***
        '''.replace('  ', ''), className='container',
                 containerProps={'style': {'maxWidth': '650px'}}),

    # html.Div([
    #     html.Iframe(srcDoc=open('JupyterNotebooks/heatmap_withtime_SFPD.html', 'r').read(),
    #                 style={'border': 'none', 'width': '50%', 'height': 500, 'display': 'inline-block'}),
    #     html.Iframe(srcDoc=open('JupyterNotebooks/popup_SFPD.html', 'r').read(),
    #                 style={'border': 'none', 'width': '50%', 'height': 500, 'display': 'inline-block'}),
    # ],),

    html.Div(children=[

        html.Div(children=[
            dcc.Markdown('''
                ### Heat Map with a time dimension
                Use the video options to loop through the tme dimension
                ***
                '''.replace('  ', ''), className='container',
                         containerProps={'style': {'maxWidth': '650px'}}),
            html.Iframe(srcDoc=open('JupyterNotebooks/heatmap_withtime_SFPD.html', 'r').read(),
                        style={'border': 'none', 'width': 700, 'height': 500, 'display': 'inline-block', 'padding': 20})
        ], style={'display': 'inline-block'}),

        html.Div(children=[
            dcc.Markdown('''
                ### Map with popups of incidents
                Click tool tips for data on each incident
                ***
                '''.replace('  ', ''), className='container',
                         containerProps={'style': {'maxWidth': '650px'}}),
            html.Iframe(srcDoc=open('JupyterNotebooks/popup_SFPD.html', 'r').read(),
                        style={'border': 'none', 'width': 700, 'height': 500, 'display': 'inline-block', 'padding': 20})
        ], style={'display': 'inline-block'})
    ], style={'text-align': 'center'}),

    html.Div(children=[], style={'border': 'none', 'height': 50}),

])


# Choose the CSS styly you like
for css in external_css:
    app.css.append_css({'external_url': css})

if __name__ == '__main__':
    app.run_server(debug=True)
