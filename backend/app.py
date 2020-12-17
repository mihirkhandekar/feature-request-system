from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Set up the SQLAlchemy Database to be a local file 'desserts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/features.db'
db = SQLAlchemy(app)


if __name__ == "__main__":

    # We need to make sure Flask knows about its views before we run
    # the app, so we import them. We could do it earlier, but there's
    # a risk that we may run into circular dependencies, so we do it at the
    # last minute here.

    from views import *

    app.run(debug=True, host= '0.0.0.0')
