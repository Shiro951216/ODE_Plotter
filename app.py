from dash import Dash, html, dcc
import dash


app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True
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
        dcc.Link(html.Button('Critical Points', className='boton edo_4'), href='/criticalPoint')
    ]),
    
    dash.page_container
])


if __name__ == '__main__':
    app.run(debug=True)
