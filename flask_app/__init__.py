from flask import Flask
app = Flask(__name__)

app.app_context().push()
from flask_bootstrap import Bootstrap


app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

