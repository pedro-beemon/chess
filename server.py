'''Aplicativo Web'''

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    'Home'

    return 'Hello world!'
