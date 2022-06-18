from flask import Flask, request, render_template, jsonify
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

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/exe_html')
def exe_html():
    return render_template('exercise.html')

@app.route('/exercise')
def my_html():
    s = request.args.get("my_name")
    return s

@app.route('/try_rest', methods=['POST'])
def try_rest():
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json": request_json}
    return jsonify(response_json)
