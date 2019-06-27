from os import getenv, path
from flask import Flask, render_template, request, json, request
from werkzeug.security import generate_password_hash
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

print(getenv('MYSQL_DATABASE_USER', ''))
print(getenv('MYSQL_DATABASE_PASSWORD', ''))
print(getenv('MYSQL_DATABASE_DB', ''))
print(getenv('MYSQL_DATABASE_HOST', ''))

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

        if (name and email and password):
            with mysql.connect() as conn:
                with conn.cursor() as cursor:

                    cursor.execute('select * from tbl_user where email %s', email)
                    result = cursor.fetchall()

                    if(len(result) > 0):
                        return json.dumps({'error':'Email já cadastrado'})
                    
                    hash_password = password #generate_password_hash(password)
                    cursor.execute('insert into tbl_user (user_name, user_email, user_password) values (%s, %s, %s)', (name, email, hash_password))
                    result = cursor.fetchall()

                    if (len(result) > 0):
                        return json.dumps({'message':'Usuário criado com sucesso!'})
                    else:
                        return json.dumps({'error': 'Erro ao salvar usuário'})
        else:
            return json.dumps({'html': '<span>Preencha os campos requeridos</span>'})
    except Exception as e:
        return json.dumps({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)