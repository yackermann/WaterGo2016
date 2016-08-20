import os

# ----- DATABASES ----- #
DATABASE    = 'flaskr.db'
USERNAME    = 'admin'
PASSWORD    = 'admin'

# defines the full path for the database
BASEDIR       = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASEDIR, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False
# ----- DATABASES ENDS ----- #