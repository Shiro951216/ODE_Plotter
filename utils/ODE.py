import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np
import sympy as sp
from sympy import symbols, sympify, Matrix, solve, simplify

def classify_point(T, D):
    # Calcular el discriminante
    delta = T**2 - 4 * D
    
    # Clasificación según T, D y delta
    if D < 0:
        return "Punto Silla (saddle point)"
    elif D > 0:
        if delta > 0:
            if T < 0:
                return "Nodo estable (atractor)"
            elif T > 0:
                return "Nodo inestable (repulsor)"
        elif delta < 0:
            if T < 0:
                return "Foco estable (espiral estable)"
            elif T > 0:
                return "Foco inestable (espiral inestable)"
            else:
                return "Centro"
        else:
            if T > 0:
                return "Nodo degenerado inestable"
            elif T < 0:
                return "Nodo degenerado estable"
            else:
                return "Flujo uniforme"
    else:
        if T > 0:
            return "Linea de puntos inestables"
        elif T < 0:
            return "Linea de puntos estables"
        else:
            return "Flujo uniforme"

    return f"Punto que no se puede clasificar"


def temp(X, Y, critical_points, sym):
    x,y = sym
    J = simplify(X.jacobian(Y))

    text = ""
    for point in critical_points:
        J_ = J.subs({x: point[0], y: point[1]})
        T = simplify(J_.trace())
        D = simplify(J_.det())
        text += f"El punto ({point[0]}, {point[1]}) es un {classify_point(T, D)}\n"

    return text

def points_ODE(dx_input, dy_input, a, b, c, d, n, scale):
    """
    Generates a vector field plot from given first-order ordinary differential equations (ODEs).
    
    Parameters:
    - dx_input (str): Expression for the change in x (dx).
    - dy_input (str): Expression for the change in y (dy).
    - a (float): Minimum value for the x and y axes.
    - b (float): Maximum value for the x and y axes.
    - n (int): Number of points to create in each dimension for the grid.

    Returns:
    - fig (plotly.graph_objects.Figure): Plotly figure containing the vector field and critical points.
    """

    fig = go.Figure()
    text = 'No se pueden clasificar'
    try:
        # Define symbols
        x_sym, y_sym = sp.symbols("x y")

        # Convert input expressions to symbolic form
        dx = sp.sympify(dx_input)
        dy = sp.sympify(dy_input)
        # Calculate critical points

        try:
            A = np.array(solve([dx, dy], (x_sym, y_sym))).astype(float)
            text = temp(Matrix([dx, dy]),Matrix([x_sym, y_sym]),A, [x_sym, y_sym])
            if text == '':
                text = 'No tiene puntos críticos, flujo uniforme'
        except:
            A = solve([dx, dy], (x_sym, y_sym), dict=True)
            critx = []
            crity = []
            for dicts in A:
                critx.append(float([*dicts.values()][0]))
                crity.append(float([*dicts.values()][1]))
            
            critp = []
            for i,e in zip(critx, crity):
                critp.append(tuple([i,e]))
            text = temp(Matrix([dx, dy]),Matrix([x_sym, y_sym]),critp, [x_sym, y_sym])
            if text == '':
                text = 'No tiene puntos críticos, flujo uniforme'
            fig.add_traces(go.Scatter(x = critx, y = crity, marker_color='rgba(255, 0, 0, 1)', mode='markers',marker=dict(size=10),
                                  name='Eq Point'))
    except:
        pass

    try:
        
        # Define symbols
        x_sym, y_sym = sp.symbols("x y")

        # Convert input expressions to symbolic form
        dx = sp.sympify(dx_input)
        dy = sp.sympify(dy_input)
        
        # Create a mesh grid for the plot
        x_vals = np.linspace(a, b, n)
        y_vals = np.linspace(c, d, n)
        X_, Y_ = np.meshgrid(x_vals, y_vals)

        # Create empty matrices to store the vector field components
        U = np.zeros_like(X_)
        V = np.zeros_like(Y_)

        for i in range(X_.shape[0]):
            for j in range(X_.shape[1]):
                U[i, j] = dx.subs({x_sym: X_[i, j], y_sym: Y_[i, j]})
                V[i, j] = dy.subs({x_sym: X_[i, j], y_sym: Y_[i, j]})

        # Normalize the vector field
        N = np.hypot(U, V) + 1e-8  # Prevent division by zero
        U_normalized = U / N
        V_normalized = V / N

        quiver = ff.create_quiver(X_ - 0.5*scale*U_normalized, Y_ - 0.5*scale*V_normalized, U_normalized, V_normalized, scale=scale,
                                line=dict(color='blue', width=1),
                                name='Vector Field')
        fig.add_traces(quiver.data)

        try:
        # Calculate critical points
            A = np.array(sp.solve([dx, dy], (x_sym, y_sym))).astype(float)
            fig.add_traces(go.Scatter(x = A[:,0], y = A[:,1], mode='markers',marker=dict(size=10),
                                  name='Eq Point'))
            
        except:
            pass

    except:
        pass
   

    fig.update_layout(
        title={
                'text': 'ODE Phase Portrait',
                'x': 0.5,
                'y': 0.92,
                'xanchor': 'center'
            },
        xaxis_title='x',
        yaxis_title='y',
        width=800,
        template='plotly_white',
        margin=dict(l=10, r=10, t=90, b=0),
        legend=dict(orientation='h', y=1.1)
    )

    # Add contours to the axes
    fig.update_xaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=True
    )
    fig.update_yaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=True
    )    

    return fig, text