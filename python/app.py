from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_mysqldb import MySQL
from pymongo import MongoClient

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '24534152'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

client = MongoClient('localhost', 27017)
mongo_db = client['trab_node']
mongo_collection = mongo_db['users']

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios")
    users = cur.fetchall()
    cur.close()
    return render_template('index.html', users=users)


@app.route('/cadastro')
def cadastro():
    return render_template('pages/cadastro.html')

@app.route('/<int:user_id>/edit', methods=['GET'])
def edit_user(user_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
        user = cur.fetchone()
        cur.close()

        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404

        return render_template('pages/editar.html', user_id=user_id, user=user)
    except Exception as e:
        return jsonify({'error': str(e)}), 500




@app.route('/users/new', methods=['POST'])
def create_user():
    if request.method == 'POST':
        user_data = {
            'nome': request.form['name'],
            'email': request.form['email'],
            'senha': request.form['password']
        }

        mysql_query = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        mysql_data = (user_data['nome'], user_data['email'], user_data['senha'])
        
        cur = mysql.connection.cursor()
        cur.execute(mysql_query, mysql_data)
        mysql.connection.commit()
        cur.close()
        
        mongo_collection.insert_one(user_data)
        
        return redirect(url_for('index'))


#Nao esta atualizando as infos no mongo, só no mysql
@app.route('/users/<int:user_id>', methods=['POST'])
def update_user(user_id):
    try:
        user_data = request.form
        mysql_query = "UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE id = %s"
        mysql_data = (user_data['name'], user_data['email'], user_data['password'], user_id)

        cur = mysql.connection.cursor()
        cur.execute(mysql_query, mysql_data)
        mysql.connection.commit()
        cur.close()

        mongo_collection.update_one({'_id': user_id}, {'$set': {'nome': user_data['name'], 'email': user_data['email'], 'senha': user_data['password']}})

        return redirect(url_for('index'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/deletar/<int:user_id>')
def deletar_usuario(user_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
        mysql.connection.commit()
        cur.close()
        
        mongo_collection.delete_one({'_id': user_id})
        
        return redirect(url_for('index'))
    except Exception as e:
        return jsonify({'error': str(e)})
    

@app.route('/redirecionar_para_login')
def redirecionar_para_login():
    return redirect('http://localhost:3000/login')

if __name__ == '__main__':
    app.run(debug=True)
