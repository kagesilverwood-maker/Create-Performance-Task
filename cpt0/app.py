
from flask import Flask, jsonify, request, send_from_directory
from pos import pos
app = Flask(__name__, static_folder='.')


#@app.route('/api/Beginner.html', methods=['GET'])
#def pos():
    #return jsonify({"message": "Tacking is when you turn your boat and the bow crosses the wind first."})

#@app.route('/api/add', methods=['POST'])
#def add():
   # data = request.get_json(force=True)
    #result = data['a'] + data['b']
    #return jsonify({"result": result})

@app.route('/style.css')
def style():
    return send_from_directory('.', 'style.css')

@app.route('/script.js')
def script():
    return send_from_directory('.', 'script.js')

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

@app.route('/api/pos', methods=['POST'])
def pos_api():
    data = request.get_json()

    wind_speed = data.get("wind_speed")
    boat_heading = data.get("boat_heading")

    result = pos(wind_speed, boat_heading)

    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True)