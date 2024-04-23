from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@app.before_request
def require_login():
    if request.endpoint != 'login' and 'authenticated' not in session:
        return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    # Fetch data from the database for students and quizzes
    return render_template('dashboard.html', students=students, quizzes=quizzes)

if __name__ == '__main__':
    app.run(debug=True)
