#ai
from flask import Flask, jsonify, request, send_from_directory
#ai ends
from pos import pos
from upwind import upwind

#ai
app = Flask(__name__, static_folder='.')

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')
#ai ends

@app.route('/home.html')
def home():
    return send_from_directory('.', 'home.html')


@app.route('/Beginner.html')
def beginner():
    return send_from_directory('.', 'Beginner.html')

@app.route('/Intermediate.html')
def intermediate():
    return send_from_directory('.', 'Intermediate.html')

@app.route('/Advanced.html')
def advanced():
    return send_from_directory('.', 'Advanced.html')

@app.route('/Activities.html')
def activities():
    return send_from_directory('.', 'Activities.html')
#ai
@app.route('/api/pos', methods=['POST'])
def pos_api():
    data = request.get_json()

    boat_heading = data.get("boat_heading")

    result = pos(boat_heading)

    return jsonify(result)

@app.route('/api/upwind', methods=['POST'])
def upwind_api():
    data =request.get_json()

    move_input= data.get("move_input")

    result= upwind(move_input)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
#ai ends