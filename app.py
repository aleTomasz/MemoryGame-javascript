
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "b6128f50-6f58-46ba-adca-a50ea3c9b9d2"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration_page.html')

@app.route('/login')
def login_page():
    return render_template('login_page.html')