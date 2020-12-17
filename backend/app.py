from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# SQLAlchemy database can be set up according to requirements
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/features.db'
db = SQLAlchemy(app)


if __name__ == "__main__":
    from views import *
    app.run(host='0.0.0.0')
