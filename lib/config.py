import os

class Config:
    # секретний ключ для безпеки сесій
    SECRET_KEY = os.environ.get('SECRET_KEY', 'cfda24b1ddc899970694e189a9140938f408678924e8887b07cf496f4020aca7c52c99cefbf796921d3a2a85194ffb75ecc6e80ee92bf7208db8a7b1cc85a6ea') 
    # налаштування бази даних
    DB_USER = os.environ.get('MYSQL_USER', 'admin2')
    DB_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    DB_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    DB_NAME = os.environ.get('MYSQL_DATABASE', 'contacts_db')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    