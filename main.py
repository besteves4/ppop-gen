from dash import Dash, html, dcc, Input, Output
from rdflib import Graph, Namespace, URIRef, BNode, Literal
from rdflib.namespace import RDF
from datetime import date

g = Graph()

odrl = Namespace("http://www.w3.org/ns/odrl/2/")
g.namespace_manager.bind('odrl', URIRef('http://www.w3.org/ns/odrl/2/'))

dpv = Namespace("https://w3id.org/dpv#")
g.namespace_manager.bind('dpv', URIRef('https://w3id.org/dpv#'))

oac = Namespace("https://w3id.org/oac/")
g.namespace_manager.bind('oac', URIRef('https://w3id.org/oac/'))

ppop = Namespace("https://w3id.org/ppop/")
g.namespace_manager.bind('ppop', URIRef('https://w3id.org/ppop/'))

dc = Namespace("http://purl.org/dc/terms/")
g.namespace_manager.bind('dc', URIRef('http://purl.org/dc/terms/'))

ex = Namespace("https://example.com/")

app = Dash(__name__)
app.layout = html.Div(
    className='wrapper',
    children=[
        html.H3('PPOP policies generator', className='main-title'),
        html.P('Prototype implementation of a generator of machine and human-readable PPOP policies', className='paragraph-lead'),
        html.Div(
            className='card',
            children=[
                html.H3('Policy description', className='card-title'),
                dcc.Textarea(
                    id='description',
                    value='This policy covers ...',
                    style={'width': '60%', 'height': 100},
                ),
                html.Br(id="placeholder_1"),html.Br(),html.Br(),
                html.Div(
                    id='button-div',
                    children=[
                        html.A("Generate offer", id="generate-btn", className='card-button'),
                        html.Br(),html.Br()
                    ]
                )
            ]
        ),
        html.Div(
            className='card',
            children=[
                html.Pre(id='generated', className='card-text', children='')
            ]
        ),
    ]
)

@app.callback(Output('placeholder_1', 'children'),
              [Input('description', 'value')])
def generate_policy(description):
    g.set((ex.policy, RDF.type, odrl.Privacy))
    #g.set((ex.policy, odrl.profile, ppop))
    #g.add((ex.policy, odrl.profile, oac))
    g.set((ex.policy, odrl.uid, URIRef("http://example.com/policy:2")))
    g.set((ex.policy, dc.description, Literal(description)))
    g.set((ex.policy, dc.issued, Literal(date.today())))
    return ;

@app.callback([Output('generated', 'children')],
              [Input('generate-btn', 'n_clicks')],
              prevent_initial_call=True)
def display_policy(n_clicks):
    a = g.serialize(format='turtle').decode("utf-8")
    return [a]

if __name__ == '__main__':
    app.run_server(debug=True)