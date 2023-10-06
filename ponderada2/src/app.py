from flask import Flask, render_template, request, redirect, url_for, session
import os
import psycopg2

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# PostgreSQL database setup
def create_table():
    conn = psycopg2.connect(
        host='postgres',
        user='teste',
        password='teste123',
        database='notes'
    )
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Table created successfully")

def get_notes():
    conn = psycopg2.connect(
        host='postgres',
        user='teste',
        password='teste123',
        database='notes'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()
    conn.close()
    return notes

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

        if username == 'your_valid_username' and password == 'your_valid_password':
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
        conn = psycopg2.connect(
            host='postgres',
            user='teste',
            password='teste123',
            database='notes'
        )
        cursor = conn.cursor()
        cursor.execute('INSERT INTO notes (title, content) VALUES (%s, %s)', (title, content))
        conn.commit()
        conn.close()

    notes = get_notes()
    return render_template('notes.html', notes=notes)

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit(note_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = psycopg2.connect(
            host='postgres',
            user='teste',
            password='teste123',
            database='notes'
        )
        cursor = conn.cursor()
        cursor.execute('UPDATE notes SET title=%s, content=%s WHERE id=%s', (title, content, note_id))
        conn.commit()
        conn.close()
        return redirect(url_for('notes'))

    conn = psycopg2.connect(
        host='postgres',
        user='teste',
        password='teste123',
        database='notes'
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes WHERE id = %s', (note_id,))
    note = cursor.fetchone()
    conn.close()

    return render_template('edit.html', note=note)

# Modify the delete route
@app.route('/delete/<int:note_id>', methods=['POST', 'DELETE'])
def delete(note_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST' or (request.method == 'POST' and request.form.get('_method') == 'DELETE'):
        conn = psycopg2.connect(
            host='postgres',
            user='teste',
            password='teste123',
            database='notes'
        )
        cursor = conn.cursor()
        cursor.execute('DELETE FROM notes WHERE id = %s', (note_id,))
        conn.commit()
        conn.close()

        return redirect(url_for('notes'))
    else:
        return "Invalid request method"

if __name__ == '__main__':
    create_table()
    app.run(debug=True, host='0.0.0.0', port=5000)