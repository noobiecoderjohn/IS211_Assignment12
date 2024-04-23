import sqlite3
from flask import Flask, request, session, g, redirect, url_for, render_template, flash

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='dev')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('hw13.db')
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    db = get_db()
    students = db.execute('SELECT * FROM students').fetchall()
    quizzes = db.execute('SELECT * FROM quizzes').fetchall()
    return render_template('dashboard.html', students=students, quizzes=quizzes)

@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        db = get_db()
        db.execute('INSERT INTO students (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
        db.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_student.html')

@app.route('/quiz/add', methods=['GET', 'POST'])
def add_quiz():
    if request.method == 'POST':
        subject = request.form['subject']
        number_of_questions = request.form['number_of_questions']
        quiz_date = request.form['quiz_date']
        db = get_db()
        db.execute('INSERT INTO quizzes (subject, number_of_questions, quiz_date) VALUES (?, ?, ?)',
                   (subject, number_of_questions, quiz_date))
        db.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_quiz.html')

if __name__ == '__main__':
    app.run(debug=True)
