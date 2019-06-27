from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/home')
def home():
    return 'home'

@app.route('/members')
def members():
    return 'members'

@app.route('/members/<string:name>')
def members_name(name: str):
    return 'member: {}'.format(name)

if __name__ == '__main__':
    app.run(port=5001)