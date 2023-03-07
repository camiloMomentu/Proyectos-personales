from dotenv import load_dotenv
import os
from conections.mongo import Mongo

load_dotenv(verbose=True)

SECRET_KEY = os.getenv('SECRET_KEY')
MONGO_URL = os.getenv('MONGO_URL')
Mongo = Mongo(MONGO_URL)

ORIGINS = [
    'http://localhost:3000'
]