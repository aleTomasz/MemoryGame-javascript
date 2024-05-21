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

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['psw']
        password_repeat = request.form['psw-repeat']
        if password == password_repeat:
            database_common.add_user(login, password)
            return redirect(url_for('login_page'))
        else:
            return render_template('registration_page.html', error="Passwords do not match")
    return render_template('registration_page.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login(cursor):
#     if request.method == 'POST':
#         login = request.form['login']
#         password = request.form['password']
#         cursor.execute("""SELECT login, password FROM users WHERE login = '{login}' and password = '{password}'""")

#propozycja
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['psw']
        # Assuming database_common handles database operations and protects against SQL injection
        user = database_common.get_user(login, password)
        if user:
            session['username'] = login
            return redirect(url_for('index'))
        else:
            # Handle invalid login
            return render_template('login_page.html', error="Invalid login credentials")
    return render_template('login_page.html')

@app.route('/login_page')
def login_page():
    return render_template('login_page.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)