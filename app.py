# Ao abrir o GitPod, execute:
# pip install -r requirements.txt
from flask import Flask, render_template

app = Flask(__name__)
clientes = [
    {'nome': 'Fulano', 'email': 'fulano@gmail.com', 'telefone': '1234567'},
    {'nome': 'Ciclano', 'email': 'Ciclano@gmail.com', 'telefone': '17988208223'}
]

@app.route('/')
def index():
    return render_template('index.html', clientes=clientes)

@app.route('/create')
def create():
    return render_template('create.html')

app.run(debug=True)