from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

SECRET_KEY = os.getenv('SECRET_KEY')
SQL_PASSWORD = os.getenv("SQL_PASSWORD")
SQL_USER = os.getenv("SQL_USER")
SQL_HOST = os.getenv("SQL_HOST")
SQL_DATABASE = os.getenv("SQL_DATABASE")

ORIGINS = [
    'http://localhost:3000'
]