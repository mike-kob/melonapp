import os
from dotenv import load_dotenv

load_dotenv('.env')

RUN_ENV = os.environ.get('RUN_ENV', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN')


