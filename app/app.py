from flask import Flask, request, jsonify
import os
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the modernized app!"

@app.route('/form', methods=['POST'])
def form():
    data = request.get_json()
    name = data.get('name')
    
    # Connect to database
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "appdb")
    )
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    db.commit()
    cursor.close()
    db.close()
    
    return jsonify({"message": f"Hello, {name}! Your data is saved."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
