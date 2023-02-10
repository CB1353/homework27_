from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Welcome to conversion system</h1>'


app.run(port=8080)
