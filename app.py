from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1><p>Welcome to your Flask application!</p>'

@app.route('/hello/<name>')
def hello_name(name):
    return f'<h1>Hello, {name}!</h1><p>Nice to meet you!</p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555) 