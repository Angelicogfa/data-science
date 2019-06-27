from os import getenv
import flask
from flask import Flask, render_template, request, json, request
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = getenv('MYSQL_DATABASE_USER', '')
app.config['MYSQL_DATABASE_PASSWORD'] = getenv('MYSQL_DATABASE_PASSWORD', '')
app.config['MYSQL_DATABASE_DB'] = getenv('MYSQL_DATABASE_DB', '')
app.config['MYSQL_DATABASE_HOST'] = getenv('MYSQL_DATABASE_HOST', '')
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/singup', methods=['GET'])
def get_singup():
    return render_template('singup.html')

@app.route('/singup', methods=['POST'])
def post_singup():
    try:
        name = request.form['inputName']
        email = request.form['inputEmail']
        password = request.form['inputPassword']

        # if name and email and password:
        #     with mysql.connect() as conn:
        #         with conn.cursor() as cursor:

        #             hash_password = generate_password_hash(password)
        #             cursor.callproc('sp_createUser', (name, email, hash_password))
        #             data = cursor.fetchall()

    except:
        pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)