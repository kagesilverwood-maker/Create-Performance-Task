
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Tacking is when you turn your boat and the bow crosses the wind first."})

@app.route('/api/add', methods=['POST'])
def add():
    data = request.get_json(force=True)
    result = data['a'] + data['b']
    return jsonify({"result": result})

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')
#@app.route('/')
#def home():
    #return send_from_directory('.', 'index.html')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

@app.route('/index.html')
def home():
    return send_from_directory('.', 'index.html')


@app.route('/Beginner.html')
def beginner():
    return send_from_directory('.', 'Beginner.html')

@app.route('/Intermediate.html')
def intermediate():
    return send_from_directory('.', 'Intermediate.html')

@app.route('/Advanced.html')
def advanced():
    return send_from_directory('.', 'Advanced.html')


if __name__ == '__main__':
    app.run(debug=True)