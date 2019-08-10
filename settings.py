import os
from dotenv import load_dotenv

load_dotenv('.env')

RUN_ENV = os.environ.get('RUN_ENV', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

DATABASE = {
    'username': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'hostname': os.environ.get('DB_HOST'),
    'dbname': os.environ.get('DB_NAME'),
}

DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{dbname}".format(**DATABASE)
