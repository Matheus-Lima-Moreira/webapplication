# Ao abrir o GitPod, execute:
# pip install -r requirements.txt
from flask import Flask, render_template, request, redirect, url_for
from uuid import uuid4
import csv

app = Flask(__name__)

teste = [{'id': uuid4(), 'email': 'matheus@gmail.com', 'senha': '1234'}]
with open('csv/login.csv','wt') as file_out:
    writer = csv.DictWriter(file_out, ['id', 'email', 'senha'])
    writer.writeheader()
    writer.writerows(teste)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    return redirect(url_for('movies'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    nome      = request.form['nome']        
    descricao = request.form['descricao']       
    data      = request.form['data']
    with open('csv/movies.csv','a+', newline='') as f:
        writer = csv.DictWriter(f, ['id', 'nome', 'descricao', 'data'])
        writer.writerow({'id': uuid4(), 'nome': nome, 'descricao': descricao, 'data':data})
    return redirect(url_for('movies'))

@app.route('/movies')
def movies():
    with open('csv/movies.csv', 'rt') as f:
        reader = csv.DictReader(f)
        return render_template('movies.html', movies=reader)

@app.route('/delete/<id>')
def delete(id):
    lines = list()
    with open('csv/movies.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie = dict(row)
            lines.append(movie)
            if movie['id'] == id:
                lines.remove(movie)

    with open('csv/movies.csv', 'w') as writeFile:
        writer = csv.DictWriter(writeFile, ['id', 'nome', 'descricao', 'data'])
        writer.writeheader()    
        writer.writerows(lines)    
    return redirect(url_for('movies'))

@app.route('/update/<id>')
def update(id):
    with open('csv/movies.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie = dict(row)
            if movie['id'] == id:
                return render_template('update.html', movie=movie)

@app.route('/updateAction/<id>', methods=['POST'])
def updateAction(id):
    lines     = list()
    nome      = request.form['nome']        
    descricao = request.form['descricao']       
    data      = request.form['data']    
    with open('csv/movies.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie = dict(row)
            if movie['id'] == id:
                lines.append({'id': id, 'nome': nome, 'descricao': descricao, 'data': data})
            else:
                lines.append(movie)

    with open('csv/movies.csv', 'w') as writeFile:
        writer = csv.DictWriter(writeFile, ['id', 'nome', 'descricao', 'data'])
        writer.writeheader()    
        writer.writerows(lines)    

    return redirect(url_for('movies'))

app.run(debug=True)

# Implementar o update (rota para mostrar os dados no form e outra para salvar os dados)