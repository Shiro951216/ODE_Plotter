import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np
import sympy as sp
from sympy import symbols, sympify, solve

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

    try:
        
        # Define symbols
        x_sym, y_sym = sp.symbols("x y")

        # Convert input expressions to symbolic form
        dx = sp.sympify(dx_input)
        dy = sp.sympify(dy_input)

        # dx_lambd = sp.lambdify((x_sym,y_sym), dx, 'numpy')
        # dy_lambd = sp.lambdify((x_sym,y_sym), dy, 'numpy')

        # # find jacobian
        # A = sp.Matrix([dx, dy])
        # X = sp.Matrix([x_sym, y_sym])
        # J = A.jacobian(X)
        # eig = J.eigenvals()
        
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

    return fig