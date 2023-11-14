from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def print_text():
    name = request.args.get('name', '')
    message = request.args.get('message', 'Давай дружить')
    return f'Hello {name}! {message}'

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)