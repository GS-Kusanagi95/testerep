# Teste funcional do dash em python
# Criado em: 20250721   Autor: Eng. Charles Ferreira
# Finalidade do programa: Implementacao de um dashboard para auditoria
# de individuos 

# Imports necessarios a implementacao
import dash
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc # type: ignore
from dash_iconify import DashIconify
from dash import Dash, Input, Output, State, dash_table, dcc, html, callback, clientside_callback
import pandas as pd # type: ignore
import uuid
from time import sleep

# Inicializa o dashboard app usando temas do dash bootstrap components
app = Dash()

# Definicoes de tema para o app
theme = {
    "fontFamily": "Montserrat, sans-serif",
    "defaultRadius": "md",
}

# ->> Aqui criamos os componentes que serao exibidos no app <<-
logo = "assets/images/laps_logo.png"

button1 = dmc.Button("Ground Truth", variant="filled", color="blue", radius="xl")
button2 = dmc.Button("Signals ACC/GYR", variant="filled", color="blue", radius="xl")
button3 = dmc.Button("Model Artifacts", variant="filled", color="red", radius="xl")
button4 = dmc.Button("Video File", variant="filled", color="green", radius="xl")

styleGrid = {
    "border": f"1px solid {dmc.DEFAULT_THEME["colors"]["red"][4]}",  # Comentar para retirar as bordas das colunas na versao final
    "textAlign": "center"
}

# ->> Aqui criamos o lay-out do app posicionando os elementos criados acima dentro de um container <<-
layout = dmc.AppShell(
    [
        dmc.AppShellHeader(
            dmc.Group(
                [
                    dmc.Group(
                        [
                            dmc.Burger(
                            id="burger",
                            size="sm",
                            hiddenFrom="sm",
                            opened=False,
                    ),
                    dmc.Image(src=logo, h=40, w=200, flex=0),
                    dmc.Title(f"Zoomies Audit Dashboard", order=1, c="blue"),
                        ]
                    ),
                ],
                justify="space-between",
                style={"flex": 1},
                h="100%",
                px="md",
            ),
        ),
                
        dmc.AppShellMain(
            dmc.Grid(
                children=[
                    dmc.GridCol(html.Div(
                    dmc.Stack(
                        [
                            button1,
                            button2,
                            button3,
                            button4
                        ]
                    ),
                        style=styleGrid), span=2),
                    dmc.GridCol(html.Div("Video Area", style=styleGrid), span=4),
                    dmc.GridCol(html.Div("Return Data 1", style=styleGrid), span=2),
                    dmc.GridCol(html.Div("Return Data 2", style=styleGrid), span=2),
                ],
                gutter="sm",
            ),
            
        ),
    ],
    header={"height": 80},
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"desktop": True, "mobile": True},
    },
    padding="md",
    id="appshell",
)

app.layout = dmc.MantineProvider(layout)

# ->> Aqui vao os callbacks (retornos ao usuario) do app <<-
#@clientside_callback


@callback(
    Output("appshell", "navbar"),
    #Output("gnd_truth", "loading"),
    Input("burger", "opened"),
    State("appshell", "navbar"),
)

# ->> Aqui vao alguns defs usados na implementacao <<-
def toggle_navbar(opened, navbar):
    navbar["collapsed"] = {"mobile": not opened, "desktop": True}
    return navbar

# Rotina de execucao do dashboard
if __name__ == '__main__':  # Se existir "__name__",...
    app.run(debug=True)  # inicializa o servidor do dash em modo debug, monta o dashboard e atualiza dinamicamente
