from flask import Flask, render_template
from flask_heroku import Heroku

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

    
if __name__ == '__main__':
    app.debug = True
    app.run()