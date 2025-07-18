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
# [1] Especifica um markdown com propriedade 'children' que formata um texto a ser exibido
markdown1 = dcc.Markdown(children='#### Current Development (v2)', style={'textAlign': 'center', 'color': 'blue'})  # (a)
markdown2 = dcc.Markdown(children='### **Choose one or more options: **', style={'textAlign': 'center', 'color': 'gold'})  # (b)
markdown3 = dcc.Markdown(children='### **Choose one option only: **', style={'textAlign': 'center', 'color': 'magenta'})  # (c)
# [2] Especifica um botao clicavel com propriedade 'children' a ser exibido
button = html.Button(children="Click here!!")
# [3] Especifica uma checklist com multiplas opcoes selecionaveis
checklist1 = dcc.Checklist(options=[' Parado', ' Senta', ' Anda', ' Trota', ' Corre', ' Late'])  # (a)
checklist2 = dcc.Checklist(options=[' Arthur', ' Brian', ' Jesus', ' Lancelot', ' Black Knight', ' Frenchmen'])  # (b)
# [4] Especifica uma lista com opcoes varias selecionaveis do tipo 'radio button'
radio = dcc.RadioItems(options=[' Parado', ' Senta', ' Anda', ' Trota', ' Corre', ' Late'])
# [5] Especifica um menu do tipo 'dropdown' com opcoes selecionaveis
dropdown = dcc.Dropdown(options=['PA', 'SE', 'AN', 'TR', 'CO', 'LA'])
# [6] Especifica um slider com inicio (min), fim (max) e passo de deslocamento (step)
slider = dcc.Slider(min=0, max=50, step=2)

# ->> Aqui criamos o lay-out do app posicionando os elementos criados acima dentro de um container <<-
app.layout = dbc.Container(  # A interface do app sera implementada dentro do container criado aqui
    [
    dcc.Markdown(children='# Test Drive App', style={'textAlign': 'center', 'color': 'green'}),  # Titulo do app (texto + formatadores)
    dbc.Row([dbc.Col([markdown1], width = 12)]),  # Cria a linha 1 e exibe [1a]
    dbc.Row([  # Cria a linha 2 logo abaixo de [1a]
        dbc.Col([dropdown], width = 3),  # Cria a coluna 1 e exibe [5] com largura da coluna = 3
        dbc.Col([slider], width = 10),  # Cria a coluna 2 e exibe [6] com largura de coluna = 10
        ]  # Finaliza as colunas da linha 2
    ),  # Finaliza a linha 2
    dbc.Row([dbc.Col([markdown2], width = 10)]),  # Cria a linha 3 e exibe [1b]
    dbc.Row([  # Cria a linha 4 logo abaixo da linha 3
        dbc.Col([checklist1], width = 6),  # Cria a coluna 1 e exibe [3a] com largura = 6
        dbc.Col([checklist2], width = 6),  # Cria a coluna 2 e exibe [3b] com largura = 6
        ]  # Finaliza as colunas da linha 4
    ),  # Finaliza a linha 4
    dbc.Row([dbc.Col([markdown3], width = 10)]),  # Cria a linha 5 e exibe [1c]
    dbc.Row([  # Cria a linha 6 logo abaixo de da linha 5
        dbc.Col([radio], width = 6),  # Cria a coluna 1 e exibe [4] com largura = 6
        ],  # Finaliza a coluna da linha 6
    ),  # Finaliza a linha 6
    dbc.Row(dbc.Col([button], width = 5))  # Cria a linha 7 e exibe [2] com largura maxima = 5
    ]
)

# Rotina de execucao do dashboard
if __name__ == '__main__':  # Se existir "__name__",...
    app.run(debug=True)  # inicializa o servidor do dash em modo debug, monta o dashboard e atualiza dinamicamente