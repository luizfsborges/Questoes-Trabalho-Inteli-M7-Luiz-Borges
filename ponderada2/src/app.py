from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import psycopg2
import jwt

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

def generate_token(username):
    token = jwt.encode({'username': username}, app.config['JWT_SECRET_KEY'], algorithm='HS256')
    return token

def decode_token(token):
    try:
        data = jwt.decode(token, app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        return data['username']
    except jwt.ExpiredSignatureError:
        return None

def get_notes():
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'postgres'),
        port=int(os.environ.get('DB_PORT', 5432)),
        user=os.environ.get('DB_USER', 'teste'),
        password=os.environ.get('DB_PASSWORD', 'teste123'),
        database=os.environ.get('DB_NAME', 'notes')
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()
    conn.close()
    return notes

@app.route('/')
def index():
    if 'jwt_token' in session:
        return redirect(url_for('notes'))
    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'teste' and password == 'teste123':
            # Authentication successful
            session['jwt_token'] = generate_token(username)
            return redirect(url_for('notes'))
        else:
            # Authentication failed
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

# Add a decorator to require authentication for the notes route
@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if 'jwt_token' not in session or not decode_token(session['jwt_token']):
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'postgres'),
            port=int(os.environ.get('DB_PORT', 5432)),
            user=os.environ.get('DB_USER', 'teste'),
            password=os.environ.get('DB_PASSWORD', 'teste123'),
            database=os.environ.get('DB_NAME', 'notes')
        )
        cursor = conn.cursor()
        cursor.execute('INSERT INTO notes (title, content) VALUES (%s, %s)', (title, content))
        conn.commit()
        conn.close()

    notes = get_notes()
    return render_template('notes.html', notes=notes)

# Add a decorator to require authentication for the edit route
@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit(note_id):
    if 'jwt_token' not in session or not decode_token(session['jwt_token']):
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'postgres'),
            port=int(os.environ.get('DB_PORT', 5432)),
            user=os.environ.get('DB_USER', 'teste'),
            password=os.environ.get('DB_PASSWORD', 'teste123'),
            database=os.environ.get('DB_NAME', 'notes')
        )
        cursor = conn.cursor()
        cursor.execute('UPDATE notes SET title=%s, content=%s WHERE id=%s', (title, content, note_id))
        conn.commit()
        conn.close()
        return redirect(url_for('notes'))

    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'postgres'),
        port=int(os.environ.get('DB_PORT', 5432)),
        user=os.environ.get('DB_USER', 'teste'),
        password=os.environ.get('DB_PASSWORD', 'teste123'),
        database=os.environ.get('DB_NAME', 'notes')
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes WHERE id = %s', (note_id,))
    note = cursor.fetchone()
    conn.close()

    return render_template('edit.html', note=note)

# Add a decorator to require authentication for the delete route
@app.route('/delete/<int:note_id>', methods=['POST', 'DELETE'])
def delete(note_id):
    if 'jwt_token' not in session or not decode_token(session['jwt_token']):
        return redirect(url_for('login'))

    if request.method == 'POST' or (request.method == 'POST' and request.form.get('_method') == 'DELETE'):
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'postgres'),
            port=int(os.environ.get('DB_PORT', 5432)),
            user=os.environ.get('DB_USER', 'teste'),
            password=os.environ.get('DB_PASSWORD', 'teste123'),
            database=os.environ.get('DB_NAME', 'notes')
        )
        cursor = conn.cursor()
        cursor.execute('DELETE FROM notes WHERE id = %s', (note_id,))
        conn.commit()
        conn.close()

        return redirect(url_for('notes'))
    else:
        return "Invalid request method"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)