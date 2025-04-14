from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>WELCOME TO SIU UNIVERSITY😂😁 <h1>      '

@app.route('/user/<name>')
def user(name):
    return f'<h2> WELCOME TO SIU, {name}<h2>     '
app.add_url_rule('/user/<name>',user)
if __name__ == '__main__':
    app.run(debug=True)