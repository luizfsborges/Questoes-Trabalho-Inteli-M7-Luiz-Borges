# src/app.py
from flask import Flask, render_template, request, redirect, url_for, session
from banco import Banco
import os

app = Flask(__name__, template_folder='../frontend/templates')

app.secret_key = 'your_secret_key'

# Sample user for authentication
VALID_USERNAME = 'teste'
VALID_PASSWORD = 'teste123'

# Define the root path for the project
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_PATH = os.path.join(ROOT_PATH, 'frontend', 'templates')

# Instantiate the Banco class
db = Banco(dbname='notes_db', user='your_username', password='your_password', host='localhost', port=5432)

def create_table():
    db.criar_tabela_notas()

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('notes'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            # Authentication successful
            session['username'] = username
            create_table()
            return redirect(url_for('notes'))
        else:
            # Authentication failed
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        db.adicionar_nota(title, content)

    notes = db.obter_notas()
    return render_template('notes.html', notes=notes)

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit(note_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        db.editar_nota(note_id, title, content)
        return redirect(url_for('notes'))

    note = db.obter_nota_por_id(note_id)
    return render_template('edit.html', note=note)

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete(note_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    db.deletar_nota(note_id)
    return redirect(url_for('notes'))

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
