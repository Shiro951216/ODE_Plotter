###################################################################################
#
# Librerías
#
###################################################################################
import dash
from dash import dcc, html, Input, Output, callback
from utils import *

dash.register_page(
    __name__,
    path='/criticalPoint',
    name='criticalPoint'
)

###################################################################################
#
# Layout HTML
#
###################################################################################

layout = html.Div(className='Pages', children=[
    html.Div(className='div_parametros', children=[
        html.H2('PARAMETERS', style={'text-align': 'center'}),

        html.Div(children=[
            html.Div(className='div_flex',
                     children=[html.Div(className='div_flex', children=[
                html.H3('dx = ', style={'text-align': 'center'}),
                dcc.Input(type='text', id='dx', debounce=True, placeholder="Enter dx expression")]),
                html.Div('',className='empty'),
            ], style={'padding': '10px'}),
            
            html.Div(className='div_flex',
                     children=[html.Div(className='div_flex', children=[
                html.H3('dy = ', style={'text-align': 'center'}),
                dcc.Input(type='text', id='dy', debounce=True, placeholder="Enter dy expression")]),  
                html.Div('',className='empty'),
            ], style={'padding': '10px'}),
        ]),
    ]),

    html.Div(className='div_grafica', children=[
        html.H2('STEADY-STATE POINTS', style={'text-align': 'center'}),
        
        html.Div(className='grafica', children=[
            dcc.Loading(type='default', children=dcc.Graph(id='figura_4'))
        ])
    ])
])


###################################################################################
#
# Callback principal
#
###################################################################################

@callback(
    Output('figura_4', 'figure'),
    Input('dx', 'value'),
    Input('dy', 'value')
)
def process_inputs(dx, dy):
    fig = points_ODE(dx, dy, 30, scale=0.2)
    return fig