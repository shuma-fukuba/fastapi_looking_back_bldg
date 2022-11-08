import os


APP_ENV = os.environ.get('APP_ENV')

DB_USER = os.environ.get('MYSQL_USER')
DB_PASSWORD = os.environ.get('MYSQL_PASSWORD')
DB_ROOT_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD')
DB_HOST = os.environ.get('MYSQL_HOST')
DB_NAME = os.environ.get('MYSQL_DATABASE')
GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN')
AUTH_SECRET_KEY = os.environ.get('AUTH_SECRET_KEY')
REACT_HOST = os.environ.get('REACT_HOST')
