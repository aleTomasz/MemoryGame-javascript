from flask import Flask, request, redirect, url_for, render_template, session
import jinja2
import database_common

app = Flask(__name__)
app.secret_key = "b6128f50-6f58-46ba-adca-a50ea3c9b9d2"


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    else:
        return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration_page.html')

@app.route('/login')
def login(cursor):
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        cursor.execute("""SELECT login, password FROM users WHERE login = '{login}' and password = '{password}'""")


if __name__ == '__main__':
    app.run(debug=True)