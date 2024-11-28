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

        html.Div(className='div_flex',children=[
            html.Div(className='div_flex',
                     children=[html.Div(className='div_flex', children=[
                html.H3('dx = ', style={'text-align': 'center'}),
                dcc.Input(type='text', id='dx', debounce=True, value='x*(y+3)',placeholder="Enter dx expression")]),
                html.Div('',className='empty'),
            ], style={'padding': '10px'}),
            
            html.Div(className='div_flex',
                     children=[html.Div(className='div_flex', children=[
                html.H3('dy = ', style={'text-align': 'center'}),
                dcc.Input(type='text', id='dy', debounce=True, value='(x-2)*y', placeholder="Enter dy expression")]),  
                html.Div('',className='empty'),
            ], style={'padding': '10px'}),
        ]),

        html.Div(className='div_flex',children=[
            html.Div(className='div_flex',
                     children=[html.Div(className='div_flex', children=[
                html.H3('x_min =  ', style={'text-align': 'center'}),
                dcc.Input(type='number', id='x_min', debounce=True, value = -5)]),
                html.Div('',className='empty'),
            ], style={'padding': '10px'}),
            
            html.Div(className='div_flex',
                     children=[html.Div(className='div_flex', children=[
                html.H3('x_max =  ', style={'text-align': 'center'}),
                dcc.Input(type='number', id='x_max', debounce=True, value = 5)]),
                html.Div('',className='empty'),
            ], style={'padding': '10px'}),
        ]),

        html.Div(className='div_flex', children=[
            html.Div(className='div_flex',
                     children=[html.Div(className='div_flex', children=[
                html.H3('y_min =', style={'text-align': 'center'}),
                dcc.Input(type='number', id='y_min', debounce=True, value = -5)]),
                html.Div('',className='empty'),
            ], style={'padding': '10px'}),
            
            html.Div(className='div_flex',
                     children=[html.Div(className='div_flex', children=[
                html.H3('y_max =  ', style={'text-align': 'center'}),
                dcc.Input(type='number', id='y_max', debounce=True, value = 5)]),
                html.Div('',className='empty'),  
            ], style={'padding': '10px'}),
        ]),
        html.Div(children=[
            html.H2('Resultados'),
            html.Pre(id='text')
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
    Output('text', 'children'),
    Input('dx', 'value'),
    Input('dy', 'value'),
    Input('x_max', 'value'),
    Input('x_min', 'value'),
    Input('y_max', 'value'),
    Input('y_min', 'value'),
)
def process_inputs(dx, dy, x_max, x_min, y_max, y_min):
    fig, text = points_ODE(dx, dy, x_min, x_max, y_min, y_max, 30, scale=0.3)
    return fig, text