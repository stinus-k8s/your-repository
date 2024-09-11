from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DATABASE_HOST', 'localhost'),
        user=os.getenv('DATABASE_USER', 'root'),
        password=os.getenv('DATABASE_PASSWORD', ''),
        database=os.getenv('DATABASE_NAME', 'test_db')
    )

@app.route('/')
def welcome():
    return 'Welcome'

@app.route('/how+are+you')
def how_are_you():
    return 'I am good, how about you?'

@app.route('/read+from+database')
def read_from_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM employees')
    result = cursor.fetchone()
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

