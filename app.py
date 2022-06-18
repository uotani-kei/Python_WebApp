from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def inex():
    return 'Response Data'

@app.route('/another')
def fla():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'

@app.route('/x_request/<user>')
def x_request(user):
    return f'x_request:{user}'

