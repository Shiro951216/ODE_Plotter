from dash import Dash, html, dcc
import dash

# external_scripts = [
#     {'src': 'https://cdn.tailwindcss.com'}
# ]

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    # external_scripts=external_scripts
)


app.layout = html.Div(className='back',children=[
    html.Div(className='header', children=[
        html.Div(className='header-content', children=[
            html.Img(className='sm_logo', src='assets/imgs/UNMSM.png'),
            html.H5('INTERFAZ GRÁFICA', className='main_title')
        ])
    ]),
    
    html.Div(className='contenedor_navegacion', children=[
        dcc.Link(html.Button('Autonomous ODE', className='boton edo_1'), href='/'),
        html.Div('',className='empty'),
        dcc.Link(html.Button('ODE System', className='boton edo_2'), href='/Edo2doOrden'),
        html.Div('',className='empty'),
        dcc.Link(html.Button('SIR Model', className='boton edo_3'), href='/SIR'),
        html.Div('',className='empty'),
        dcc.Link(html.Button('Critical Points', className='boton edo_4'), href='/criticalPoint'),
        html.Div('',className='empty'),
        dcc.Link(html.Button('SEIARS', className='boton edo_5'), href='/project')
    ]),
    
    html.Div(children=[dash.page_container],
             style={'margin-left': 'auto', 'margin-right': 'auto', 'padding-left':'0.5rem', 'padding-right':'0.5rem',
                'padding-top':'1rem', 'padding-bottom':'1rem'}),

    html.Div(children=[
        html.Div(children=[
            html.P(children=[
                html.Strong("Alumno: "),
                html.Span("Vilchez Quispe, Yoshiro Cardich")
            ]),
            html.P(children=[
                html.Strong("Código: "),
                html.Span("22140122")
            ]),
        ], style = {'height': '100%', 'display':'flex', 'flex-direction':'row',
                    'justify-content':'center', 'items-align':'center', 'gap':'40rem', 'color':'rgb(255 255 255)',
                    'font-size': '1.125rem', 'line-height': '1.75rem'}),
    ], style = {'margin-left': 'auto', 'margin-right': 'auto', 'height':'2.5rem', 'margin-top':'0.5rem', 'padding-left':'0.5rem', 'padding-right':'0.5rem',
                'padding-top':'1rem', 'padding-bottom':'2rem', 'background-color': 'rgb(0 0 0)'})
])


if __name__ == '__main__':
    app.run(debug=True)
