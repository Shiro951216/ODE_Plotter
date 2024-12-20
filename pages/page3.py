###################################################################################
#
# Librerías
#
###################################################################################
import dash
from dash import dcc, html, Input, Output, callback, ctx
from utils import *

dash.register_page(
    __name__,
    path='/SIR',
    name='Edo-Ejemplo 3'
)

###################################################################################
#
# Layout HTML
#
###################################################################################

layout = html.Div(className='Pages', children=[
        html.Div(className='div_parametros', children=[

        html.H2('PARAMETERS', style={'text-align': 'center'}),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Initial Population'),
                dcc.Input(type='number', value=1500, id='initial_population', debounce=True, step=1, min=0)  
            ]),
            html.Div([
                html.H3('Initial Infected Population'),
                dcc.Input(type='number', value=1, id='infected_population', debounce=True, step=1, min=1)  
            ]),
            html.Div([
                html.H3('Initial Recovery Population'),
                dcc.Input(type='number', value=0, id='recovery_population', debounce=True, step=1, min=0) 
            ]),
        ]),
        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Initial Transmission Rate'),
                dcc.Input(type='number', value=0.00050, id='transmission_rate', debounce=True, step=0.00001, min=0) 
            ]),
            html.Div([
                html.H3('Initial Recovery Rate'),
                dcc.Input(type='number', value=0.01, id='recovery_rate', debounce=True, step=0.001, min=0) 
            ]),
            html.Div([
                html.H3('Time'),
                dcc.Input(type='number', value=100, id='time', debounce=True, step=1, min=0)  
            ]),
        ]),

        html.Br(),

        html.Div(className='div_flex', children=[
            html.Div([
                dcc.Checklist(
                    options=[{'label': 'Change Time', 'value': 't_change'}],
                    value = [],
                    id='change_time_checkbox',
                ),
                dcc.Input(type='number', id='change_time', step=1, min=0, disabled=True, debounce=True, placeholder="Enter value")
            ]),
            html.Div([
                html.H3('New Transmission Rate'),
                dcc.Input(type='number', id='new_transmission_rate', step=0.00001, min=0, disabled=True, debounce=True, placeholder="Enter value")  
            ]),

            html.Div([
                html.H3('New Recovery Rate'),
                dcc.Input(type='number', id='new_recovery_rate', step=0.001, min=0, disabled=True, debounce=True, placeholder="Enter value")  
            ]),

        ]),
    ]),

    html.Div(className='div_grafica', children=[
        html.H2('SIR Model with Parameter Change', style={'text-align': 'center'}),
        
        html.Div(className='grafica', children=[
            dcc.Loading(type='default', children=dcc.Graph(id='figura_3'))
        ])
    ])
])

###################################################################################
#
# Callback para habilitar/deshabilitar los inputs
#
###################################################################################

@callback(
    Output('change_time', 'disabled'),
    Output('new_transmission_rate', 'disabled'),
    Output('new_recovery_rate', 'disabled'),
    Input('change_time_checkbox', 'value')
)
def toggle_inputs(change_time_checkbox):
    # Habilitar o deshabilitar los inputs basados en los checkboxes
    enabled = 't_change' in change_time_checkbox
    return [not enabled, not enabled, not enabled]

###################################################################################
#
# Callback principal
#
###################################################################################

@callback(
    Output('figura_3', 'figure'),
    Input('change_time_checkbox', 'value'),
    Input('initial_population', 'value'),
    Input('infected_population', 'value'),
    Input('recovery_population', 'value'),
    Input('transmission_rate', 'value'),
    Input('recovery_rate', 'value'),
    Input('time', 'value'),
    Input('change_time', 'value'),
    Input('new_transmission_rate', 'value'),
    Input('new_recovery_rate', 'value'),
)
def grafic_SIR_model(check, N, I, R, beta, gamma, t, change_time=None, new_beta=None, new_gamma=None):
    S = N - I - R

    # Generate the graph with the SIR model
    enable = 't_change' in check
    if not enable:
        fig = model_SIR([S, I, R], beta, gamma, t)
    else:
        # Set defaults if None
        if change_time is None or change_time == '':
            change_time = t  # or a sensible default like 100
        if new_beta is None or new_beta == '':
            new_beta = beta  # Default to original beta
        if new_gamma is None or new_gamma == '':
            new_gamma = gamma  # Default to original gamma
        fig = model_SIR([S, I, R], beta, gamma, t, change_time, new_beta, new_gamma)

    return fig