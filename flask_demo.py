from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World!<h1>'
@app.route('/hello/<name>')
def username(name):
    #print(f"Username: {name}")
    return f'<h2>Hello, {name}<h2>'
if __name__ == '__main__':
    app.run(debug=True)
