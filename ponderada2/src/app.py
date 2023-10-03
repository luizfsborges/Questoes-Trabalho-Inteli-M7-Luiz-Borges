from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample user for authentication
VALID_USERNAME = 'teste'
VALID_PASSWORD = 'teste123'

# Define the root path for the project
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# SQLite database setup
def create_table():
    db_path = os.path.join(ROOT_PATH, 'notes.db')
    print(f"Database path: {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Table created successfully")

def get_notes():
    conn = sqlite3.connect(os.path.join(ROOT_PATH, 'notes.db'))
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
        conn = sqlite3.connect(os.path.join(ROOT_PATH, 'notes.db'))
        cursor = conn.cursor()
        cursor.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
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
        conn = sqlite3.connect(os.path.join(ROOT_PATH, 'notes.db'))
        cursor = conn.cursor()
        cursor.execute('UPDATE notes SET title=?, content=? WHERE id=?', (title, content, note_id))
        conn.commit()
        conn.close()
        return redirect(url_for('notes'))

    conn = sqlite3.connect(os.path.join(ROOT_PATH, 'notes.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes WHERE id = ?', (note_id,))
    note = cursor.fetchone()
    conn.close()

    return render_template('edit.html', note=note)

# Modify the delete route in app.py
@app.route('/delete/<int:note_id>', methods=['POST', 'DELETE'])
def delete(note_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST' or (request.method == 'POST' and request.form.get('_method') == 'DELETE'):
        conn = sqlite3.connect(os.path.join(ROOT_PATH, 'notes.db'))
        cursor = conn.cursor()
        cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        conn.commit()
        conn.close()

        return redirect(url_for('notes'))
    else:
        return "Invalid request method"

if __name__ == '__main__':
    create_table()
    app.run(debug=True)