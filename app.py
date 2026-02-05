from flask import Flask, jsonify, request, g
from dotenv import load_dotenv
import os
import jwt
import psycopg2
import psycopg2.extras
import bcrypt
from auth_middleware import token_required
from auth_blueprint import authentication_blueprint

load_dotenv()

app = Flask(__name__)
app.register_blueprint(authentication_blueprint)


def get_db_connection():
    connection = psycopg2.connect(
        host='localhost',
        database=os.getenv('POSTGRES_DATABASE'),
        user=os.getenv('POSTGRES_USERNAME'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    return connection


app.run(debug=True, port=5000)
