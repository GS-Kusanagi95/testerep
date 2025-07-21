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
app = Dash()

# Definicoes de tema para o app
theme = {
    "fontFamily": "Montserrat, sans-serif",
    "defaultRadius": "md",
}

# ->> Aqui criamos os componentes que serao exibidos no app <<-
logo = "assets/images/laps_zoomies_logo1.png"
# buttons = [
#     dmc.Button("Annotated", variant="subtle", color="blue"),
#     dmc.Button("Signals", variant="subtle", color="blue"),
#     dmc.Button("Artifacts", variant="subtle", color="red"),
#     dmc.Button("Video", variant="subtle", color="green"),
# ]
button1 = dmc.Button("Annotated", variant="filled", color="blue", radius="sm" )
button2 = dmc.Button("Signals", variant="subtle", color="blue")
button3 = dmc.Button("Artifacts", variant="subtle", color="red")
button4 = dmc.Button("Video", variant="subtle", color="green")

styleGrid = {
    "border": f"1px solid {dmc.DEFAULT_THEME["colors"]["red"][4]}",
    "textAlign": "center"
}

# ->> Aqui criamos o lay-out do app posicionando os elementos criados acima dentro de um container <<-
# app.layout = dmc.MantineProvider(
#     forceColorScheme="dark",
#     children=[
#         dmc.Button(
#             "Config",
#             variant="filled",
#             color="red",
#             size="md",
#             radius="xl",
#             loading=False,
#             disabled=False,
#         ),
#         dmc.Checkbox(
#             classNames={"root": "dmc-api-demo-root"},
#             label="Check something",
#             w=200
#         ),
#     ],
#     defaultColorScheme='dark',
#     theme=theme
# )

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
                    # dmc.Group(
                    #     children=buttons,
                    #     ml="xl",
                    #     gap=0,
                    #     visibleFrom="sm"
                    # ),
                ],
                justify="space-between",
                style={"flex": 1},
                h="100%",
                px="md",
            ),
        ),
        # dmc.AppShellNavbar(
        #     id="navbar",
        #     children=buttons,
        #     py="md",
        #     px=4,
        # ),
                
        dmc.AppShellMain(
            #"There is no spoon! (The Shining Boy to Neo in the Oracle's house)"
            dmc.Grid(
                children=[
                    dmc.GridCol(html.Div([  # Aqui os botoes sao dispostos como um array
                        button1,
                        button2,
                        button3,
                        button4
                        ],
                        style=styleGrid), span=2),
                    dmc.GridCol(html.Div("2", style=styleGrid), span=4),
                    dmc.GridCol(html.Div("3", style=styleGrid), span=2),
                    dmc.GridCol(html.Div("4", style=styleGrid), span=2),
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
@callback(
    Output("appshell", "navbar"),
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