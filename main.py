from dash import Dash, html, dcc, Input, Output
from rdflib import Graph, Namespace, URIRef, BNode, Literal
from rdflib.namespace import RDF
from datetime import date

g = Graph()

odrl = Namespace("http://www.w3.org/ns/odrl/2/")
g.namespace_manager.bind('odrl', URIRef('http://www.w3.org/ns/odrl/2/'))

dpv = Namespace("https://w3id.org/dpv#")
g.namespace_manager.bind('dpv', URIRef('https://w3id.org/dpv#'))

dpvpd = Namespace("http://www.w3id.org/dpv/dpv-pd#")
g.namespace_manager.bind('dpv-pd', URIRef('http://www.w3id.org/dpv/dpv-pd#'))

dpvgdpr = Namespace("https://www.w3id.org/dpv/dpv-gdpr#")
g.namespace_manager.bind('dpv-gdpr', URIRef('https://www.w3id.org/dpv/dpv-gdpr#'))

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
                html.Br(),html.Br(),
                html.H3('Data Controller', className='card-title'),
                dcc.Input(
                    id="controller-name",
                    type="text", size="45",
                    placeholder="Controller name"
                ),
                html.Br(),
                dcc.Input(
                    id="controller-address",
                    type="text", size="45",
                    placeholder="Controller address"
                ),
                html.Br(),
                dcc.Input(
                    id="controller-email",
                    type="text", size="45",
                    placeholder="Controller email"
                ),
                html.Br(),
                dcc.Input(
                    id="dpo-name",
                    type="text", size="45",
                    placeholder="Data Protection Officer name"
                ),
                html.Br(),
                dcc.Input(
                    id="dpo-address",
                    type="text", size="45",
                    placeholder="Data Protection Officer address"
                ),
                html.Br(),
                dcc.Input(
                    id="dpo-email",
                    type="text", size="45",
                    placeholder="Data Protection Officer email"
                ),
                html.Br(),html.Br(),
                html.H3('Permission 1', className='card-title'),
                html.P('Personal Data:'),
                dcc.Dropdown(
                    id = "personal-data",
                    options = [
                        {'label': 'Age', 'value': 'http://www.w3id.org/dpv/dpv-pd#Age'},
                        {'label': 'Contact', 'value': 'http://www.w3id.org/dpv/dpv-pd#Contact'},
                        {'label': 'Dislike', 'value': 'http://www.w3id.org/dpv/dpv-pd#Dislike'}],
                    value = [],
                    multi=True
                ),
                html.P('Processing activities:'),
                dcc.Dropdown(
                    id = "processing",
                    options = [
                        {'label': 'Use', 'value': 'https://w3id.org/dpv#Use'},
                        {'label': 'Collect', 'value': 'https://w3id.org/dpv#Collect'}],
                    value = [],
                    multi=True
                ),
                html.P('Storage:'),
                dcc.Input(
                    id="storage-location",
                    type="text", size="45",
                    placeholder="Storage location"
                ),
                html.Br(),
                dcc.Input(
                    id="storage-duration",
                    type="text", size="45",
                    placeholder="Storage duration"
                ),
                html.Br(),
                dcc.Input(
                    id="storage-deletion",
                    type="text", size="45",
                    placeholder="Storage deletion"
                ),
                html.P('Purpose for processing:'),
                dcc.Dropdown(
                    id = "purpose",
                    options = [
                        {'label': 'Account Management', 'value': 'https://w3id.org/dpv#AccountManagement'},
                        {'label': 'Human Resource Management', 'value': 'https://w3id.org/dpv#HumanResourceManagement'}],
                    value = ''
                ),
                html.P('Legal basis for processing:'),
                dcc.Dropdown(
                    id = "legal-basis",
                    options = [
                        {'label': 'Consent', 'value': 'https://www.w3id.org/dpv/dpv-gdpr#A6-1-a-explicit-consent'}],
                    value = ''
                ),
                html.P('Recipient:'),
                dcc.Input(
                    id="recipient",
                    type="text", size="45",
                    placeholder="Recipient name"
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
              [Input('description', 'value'),
               Input('controller-name', 'value'),
               Input('controller-address', 'value'),
               Input('controller-email', 'value'),
               Input('dpo-name', 'value'),
               Input('dpo-address', 'value'),
               Input('dpo-email', 'value'),
               Input('personal-data', 'value'),
               Input('processing','value'),
               Input('storage-location', 'value'),
               Input('storage-duration', 'value'),
               Input('storage-deletion', 'value'),
               Input('purpose', 'value'),
               Input('legal-basis', 'value'),
               Input('recipient', 'value')])
def generate_policy(description, controller_name, controller_address, controller_email,
                    dpo_name, dpo_address, dpo_email, personal_data,
                    processing, storage_location, storage_duration, storage_deletion,
                    purpose, legalBasis, recipient):
    g.set((ex.policy, RDF.type, odrl.Privacy))
    #g.set((ex.policy, odrl.profile, ppop))
    #g.add((ex.policy, odrl.profile, oac))
    g.set((ex.policy, odrl.uid, URIRef("http://example.com/policy:2")))
    g.set((ex.policy, dc.description, Literal(description)))
    g.set((ex.policy, dc.issued, Literal(date.today())))
    g.set((ex.policy, odrl.assigner, BNode("controller")))
    g.set((ex.policy, odrl.permission, BNode("permission")))
    
    g.set((BNode("controller"), RDF.type, oac.DataController))
    g.set((BNode("controller"), dpv.hasName, Literal(controller_name)))
    g.set((BNode("controller"), dpv.hasAddress, Literal(controller_address)))
    g.set((BNode("controller"), dpv.hasContact, Literal(controller_email)))
    g.set((BNode("controller"), dpv.hasDataProtectionOfficer, BNode("dpo")))
    
    g.set((BNode("dpo"), RDF.type, dpv.DataProtectionOfficer))
    g.set((BNode("dpo"), dpv.hasName, Literal(dpo_name)))
    g.set((BNode("dpo"), dpv.hasAddress, Literal(dpo_address)))
    g.set((BNode("dpo"), dpv.hasContact, Literal(dpo_email)))
    
    g.set((BNode("permission"), ppop.accountableParty, BNode("controller")))
    g.set((BNode("permission"), odrl.target, BNode("personaldata")))
    g.set((BNode("permission"), odrl.action, BNode("action-constraints")))
    
    g.set((BNode("personaldata"), RDF.type, oac.PersonalData))
    for data in personal_data:
        g.add((BNode("personaldata"), dpv.hasPersonalData, URIRef(data)))
    
    g.set((BNode("action-constraints"), RDF.value, BNode("processing")))
    g.set((BNode("action-constraints"), odrl.refinement, BNode("constraints")))
    
    for proc in processing:
        g.add((BNode("processing"), RDF.type, URIRef(proc)))
    g.set((BNode("processing"), dpv.hasStorage, BNode("location")))
    g.add((BNode("processing"), dpv.hasStorage, BNode("duration")))
    g.add((BNode("processing"), dpv.hasStorage, BNode("deletion")))
    
    g.set((BNode("location"), RDF.type, dpv.StorageLocation))
    g.set((BNode("location"), dpv.hasLocation, Literal(storage_location)))
    
    g.set((BNode("duration"), RDF.type, dpv.StorageDuration))
    g.set((BNode("duration"), dpv.hasDuration, Literal(storage_duration)))
    
    g.set((BNode("deletion"), RDF.type, dpv.StorageDeletion))
    g.set((BNode("deletion"), dpv.hasTechnicalMeasure, Literal(storage_deletion)))
    
    g.set((BNode("constraints"), URIRef("http://www.w3.org/ns/odrl/2/and"), BNode("purpose")))
    g.add((BNode("constraints"), URIRef("http://www.w3.org/ns/odrl/2/and"), BNode("legalBasis")))
    g.add((BNode("constraints"), URIRef("http://www.w3.org/ns/odrl/2/and"), BNode("recipient")))
    
    g.set((BNode("purpose"), RDF.type, odrl.Constraint))
    g.set((BNode("purpose"), odrl.leftOperand, oac.Purpose))
    g.set((BNode("purpose"), odrl.operator, odrl.isA))
    g.set((BNode("purpose"), odrl.rightOperand, URIRef(purpose)))
    
    g.set((BNode("legalBasis"), RDF.type, odrl.Constraint))
    g.set((BNode("legalBasis"), odrl.leftOperand, ppop.LegalBasis))
    g.set((BNode("legalBasis"), odrl.operator, odrl.isA))
    g.set((BNode("legalBasis"), odrl.rightOperand, URIRef(legalBasis)))
    
    g.set((BNode("recipient"), RDF.type, odrl.Constraint))
    g.set((BNode("recipient"), odrl.leftOperand, oac.Recipient))
    g.set((BNode("recipient"), odrl.operator, odrl.eq))
    g.set((BNode("recipient"), odrl.rightOperand, Literal(recipient)))
    
    return ;

@app.callback([Output('generated', 'children')],
              [Input('generate-btn', 'n_clicks')],
              prevent_initial_call=True)
def display_policy(n_clicks):
    a = g.serialize(format='turtle').decode("utf-8")
    return [a]

if __name__ == '__main__':
    app.run_server(debug=True)