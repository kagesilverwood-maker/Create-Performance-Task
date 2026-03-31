The following is a very simple web application stack that I have generated. Please explain to me how to make a simple button application work?

script.js:

function getMessage() {
    fetch('http://127.0.0.1:5000/api/hello')
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').innerText = data.message;
        });
}

function addNumbers() {
    const a = parseInt(document.getElementById('a').value);
    const b = parseInt(document.getElementById('b').value);

    fetch('http://127.0.0.1:5000/api/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ a: a, b: b })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = "Result: " + data.result;
    });
}

app.py

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Python!"})

@app.route('/api/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)

index.html

<!DOCTYPE html>
<html>
<head>
    <title>My Project</title>
</head>
<body>
    <h1>Python + JavaScript Demo</h1>

    <button onclick="getMessage()">Get Message</button>
    <p id="output"></p>

    <h2>Add Numbers</h2>
    <input id="a" type="number" placeholder="A">
    <input id="b" type="number" placeholder="B">
    <button onclick="addNumbers()">Add</button>

    <p id="result"></p>

    <script src="script.js"></script>
</body>
</html>