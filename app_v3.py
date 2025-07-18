# Teste funcional do dash em python
# Criado em: 20250718   Autor: Eng. Charles Ferreira
# Finalidade do programa: Este programa visa testar o ambiente dash para cons-
# trucao de um aplicativo responviso para auditoria 

# Imports necessarios a implementacao
import dash
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc # type: ignore
from dash_iconify import DashIconify
from dash import Dash, Input, Output, State, dash_table, dcc, html, callback, clientside_callback

# Inicializa o dashboard app usando temas do dash bootstrap components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# ->> Aqui criamos os componentes que serao exibidos no app <<-
markdown1 = dcc.Markdown(children='#### Current Development (v3)', style={'textAlign': 'center', 'color': 'red'}) # [1]
markdown2 = dcc.Markdown(children='##### **Input Data: **', style={'textAlign': 'center', 'color': 'black'}) # [2]
markdown3 = dcc.Markdown(children='##### **Video controls **', style={'textAlign': 'center', 'color': 'black'}) # [3]
button1 = html.Button(children="Load annotated")  # [4]
button2 = html.Button(children="Load signals")  # [5]
button3 = html.Button(children="Load artifacts")  # [6]
button4 = html.Button(children="Play/Pause")  # [7]
ctrlSlider = dcc.Slider(min=10, max=60, step=5)  # [8]

# ->> Aqui criamos o lay-out do app posicionando os elementos criados acima dentro de um container <<-
app.layout = dbc.Container(  # A interface do app sera implementada dentro do container criado aqui
    [
    dcc.Markdown(children='# Zoomies Audit Dashboard', style={'textAlign': 'center', 'color': 'blue'}),  # Titulo do app (texto + formatadores)
    dbc.Row([
        dbc.Col([markdown1], width = 12)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Row([markdown2]),
            dbc.Row([button1]),
            dbc.Row([button2]),
            dbc.Row([button3])
        ], width = 4)
    ])
    
    
    ]
)
#, width = 1
# Rotina de execucao do dashboard
if __name__ == '__main__':  # Se existir "__name__",...
    app.run(debug=True)  # inicializa o servidor do dash em modo debug, monta o dashboard e atualiza dinamicamente