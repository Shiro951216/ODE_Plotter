import dash
from dash import dcc, html, Input, Output, callback
from utils import *

dash.register_page(
    __name__,
    path='/project',
    name='Proyecto Modelos'
)

layout = html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                    children="Modelo virus informático SEIARS",
                                    style = {'font-weight':'bold','font-size': '1.5rem','line-height': '2rem'}),
                            html.Div(
                                    children=[
                                                # Imagen 1
                                                html.Img(
                                                    src='/assets/model.png', 
                                                    alt='Imagen de modelo',
                                                    style= {'width': '30rem'} 
                                                ),
                                                # Imagen 2
                                                html.Img(
                                                    src='/assets/model1.png', 
                                                    alt='Imagen de modelo',
                                                    style= {'width': '30rem'} 
                                                )
                                            ],
                                            style = {'display':'flex', 'gap':'2.25rem'}
                                    ),
                    ], style={'display':'flex', 'flex-direction': 'column', 'gap':'2.25rem', 'align-items':'center'}),
    html.Div(
        children=[
        html.Div(children=[
            html.H2(children='Parámetros',
                    style = {'font-weight':'bold', 'text-align':'center', 'font-size': '1.5rem','line-height': '2rem'}),
            html.Div(
                children=[
                # Parámetros generales
                html.Div(
                    children=[
                        html.Div([
                            html.H3(children='Población inicial', style={'font-weight': '600'}),
                            dcc.Input(type='number', value=1000, id='pob_ini', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                        ]),
                        html.Div([
                            html.H3(children='Expuestos'),
                            dcc.Input(type='number', value=0, id='pob_exp', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                        ]),
                        html.Div([
                            html.H3(children='Infectados'),
                            dcc.Input(type='number', value=1, id='pob_inf', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                        ]),
                        html.Div([
                            html.H3(children='Asintomáticos'),
                            dcc.Input(type='number', value=1, id='pob_asin', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                        ]),
                        html.Div([
                            html.H3(children='Recuperados'),
                            dcc.Input( type='number', value=0, id='pob_rec', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                        ]),
                        html.Div([
                            html.H3(children='Tiempo'),
                            dcc.Input( type='number', value=10, id='tiempo', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                        ]),
                ], style={'flex':'1 1 0%', 'margin-top':'0.25rem'}),
                # Parámetros adicionales
                html.Div(children=[
                    html.Div([
                        html.H3(children='Lambda (Λ)'),
                        dcc.Input( type='number', value=0.0613, id='Lambda', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                    ]),
                    html.Div([
                        html.H3(children='mu'),
                        dcc.Input( type='number', value=0.0688, id='mu', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                    ]),
                    html.Div([
                        html.H3(children='lambda'),
                        dcc.Input( type='number', value=0.35, id='lambda1', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                    ]),
                    html.Div([
                        html.H3(children='xi1'),
                        dcc.Input( type='number', value=0.08, id='xi1', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                    ]),
                    html.Div([
                        html.H3(children='xi2'),
                        dcc.Input( type='number', value=0.07, id='xi2', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                    ]),
                    html.Div([
                        html.H3(children='beta'),
                        dcc.Input( type='number', value=0.01, id='beta', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                    ]),
                ], style={'flex':'1 1 0%', 'margin-top':'0.25rem'}),
                html.Div(children=[
                    html.Div([
                        html.H3(children='rho1'),
                        dcc.Input(type='number', value=0.7, id='rho1', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                    ]),
                    html.Div([
                        html.H3(children='rho2'),
                        dcc.Input(type='number', value=0.05, id='rho2', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                    ]),
                    html.Div([
                        html.H3(children='alpha'),
                        dcc.Input(type='number', value=0.75, id='alpha', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                    ]),
                    html.Div([
                        html.H3(children='delta'),
                        dcc.Input(type='number', value=0.04, id='delta', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                    ]),
                    html.Div([
                        html.H3(children='psi'),
                        dcc.Input(type='number', value=0.1, id='psi', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                    ]),
                    html.Div([
                        html.H3(children='eta'),
                        dcc.Input(type='number', value=0.001, id='eta', debounce=True, style={'width':'100%', 'font-size': '0.875rem', 'line-height': '1.25rem', 'padding-left': '0.5rem', 'padding-right':'0.5rem',
                                'padding-top': '0.25rem', 'padding-bottom':'0.25rem', 'border-width': '1px', 'border-color': 'rgb(156 163 175)' })
                    ]),
                ], style={'flex':'1 1 0%', 'margin-top':'0.25rem'}),
            ], style= {'display':'flex', 'gap':'2.5rem'}),
        ], style = {'margin-top': '0.75rem'}),
        html.Div(children=[
            html.Span(children="Tasa de reproducción básica: "),
            html.Span(id="basic"),
        ], style = {'font-weight': 'bold'}),
        # Sección de gráfica
        html.Div(children=[
            html.H2(children='Resultados',
                    style = {'font-weight':'bold', 'text-align':'center', 'font-size': '1.5rem','line-height': '2rem'}),
            html.Div(children=[
                html.Div(children=dcc.Loading(type='default', children=dcc.Graph(id='COMPLETO')), style = {'grid-column': 'span 6 / span 6'}),
                html.Div(children=dcc.Loading(type='default', children=dcc.Graph(id='suceptibles')), style = {'grid-column': 'span 2 / span 2'}),
                html.Div(children=dcc.Loading(type='default', children=dcc.Graph(id='expuesto')), style = {'grid-column': 'span 2 / span 2'}),
                html.Div(children=dcc.Loading(type='default', children=dcc.Graph(id='infectado')), style = {'grid-column': 'span 2 / span 2'}),
                html.Div(children=dcc.Loading(type='default', children=dcc.Graph(id='asintomatico')), style = {'grid-column': 'span 3 / span 3'}),
                html.Div(children=dcc.Loading(type='default', children=dcc.Graph(id='recuperado')), style = {'grid-column': 'span 3 / span 3'}),
            ], style = {'display':'grid', 'grid-template-columns':'repeat(6, minmax(0, 1fr))', 'gap':'1.5rem'})
        ], style = {'flex':'1 1 0%'})
    ], style = {'display':'flex', 'flex-direction':'column', 'gap':'1.5rem'})
], style={'margin-top': '2.25rem'})
###################################################################################
#
# Callback principal
#
###################################################################################
@callback(
    Output('COMPLETO', 'figure'),
    Output('suceptibles', 'figure'),
    Output('expuesto', 'figure'),
    Output('infectado', 'figure'),
    Output('asintomatico', 'figure'),
    Output('recuperado', 'figure'),
    Output('basic', 'children'),
    Input('pob_ini', 'value'),
    Input('pob_exp', 'value'),
    Input('pob_inf', 'value'),
    Input('pob_asin', 'value'),
    Input('pob_rec', 'value'),
    Input('tiempo', 'value'),
    Input('Lambda', 'value'),
    Input('mu', 'value'),
    Input('lambda1', 'value'),
    Input('xi1', 'value'),
    Input('xi2', 'value'),
    Input('beta', 'value'),
    Input('rho1', 'value'),
    Input('rho2', 'value'),
    Input('alpha', 'value'),
    Input('delta', 'value'),
    Input('psi', 'value'),
    Input('eta', 'value'),
)
def grafic_SIR_model(N, E, I, A, R, t, Lambda, mu, lambda1, xi1, xi2, beta, p1, p2, alpha, delta, psi, eta):
    # Initial populations and parameters
    S = N - E - I - A - R
    populations = [S, E, I, A, R]
    xi = [xi1, xi2]
    p = [p1, p2]

    # Generate the graphs
    fig, R_0 = SIARS(populations, t, Lambda, mu, lambda1, xi, beta, p, alpha, delta, psi, eta)
    
    # Unpack the figures
    fig_t = fig[0]  # Combined figure
    individual_figs = fig[1]  # List of individual compartment figures

    # Return the combined figure for the 'COMPLETO' graph, and the individual graphs for the others
    return fig_t, individual_figs[0], individual_figs[1], individual_figs[2], individual_figs[3], individual_figs[4], R_0