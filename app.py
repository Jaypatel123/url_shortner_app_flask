from flask import Flask, render_template

app = Flask(__name__)

print(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return "this is url shortner"