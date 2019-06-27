from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask app'

@app.route('/hello/<string:name>')
def hello(name: str):
    return render_template('template2.html', name = name)

if __name__ == '__main__':
    app.run()
