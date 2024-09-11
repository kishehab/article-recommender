from flask import Flask, request, jsonify, render_template
from tinydb import TinyDB, Query

app = Flask(__name__)

# Initialize TinyDB (stores data in a JSON file)
db = TinyDB('db.json')

@app.route('/')
def home():
    user = 'Alice'
    is_logged_in = True
    return render_template('index.html', user=user, is_logged_in=is_logged_in)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')
    
    # Insert user into TinyDB
    db.insert({'name': name, 'age': age, 'city': city})
    
    return jsonify({'message': 'User added successfully!'})

@app.route('/list_users', methods=['GET'])
def list_users():
    # Retrieve all users
    users = db.all()
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)

