from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    return 'Olá, mundo! Este é o seu primeiro app Flask!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)