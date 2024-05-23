from flask import Flask, request, redirect, url_for, render_template, session, make_response
import data_menager  # Poprawka: zmiana na data_manager

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
            #2database_common.add_user(login, password)
            data_menager.add_user(login, password)  # Poprawka: zmiana na data_manager
            return redirect(url_for('login_page'))
        else:
            return render_template('registration_page.html', error="Passwords do not match")
    return render_template('registration_page.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['psw']
        # Assuming database_common handles database operations and protects against SQL injection
        user = data_menager.get_user(login, password)
        if user:
            session['username'] = user["login"]
            session['id'] = user["id"]
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

@app.route('/score', methods=['POST'])
def score():
    score = request.form['score']
    id = session['id']
    data_menager.set_score(id, score)
    return make_response()

@app.route('/ranking')
def ranking():
    ranking = data_menager.ranking()
    return render_template('ranking.html', ranking=ranking)


if __name__ == '__main__':
    app.run(debug=True)
