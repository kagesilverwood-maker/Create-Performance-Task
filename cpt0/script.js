function tacking() {
    fetch('http://127.0.0.1:5000/api/hello')
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').innerText = data.message;
        });
}

function addNumbers() {
    const a = parseInt(document.getElementById('a').value);
    const b = parseInt(document.getElementById('b').value);

    // explain to mr hicks what this does? He thinks it is related to flask
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
<script src="/script.js"></script>
function home(){
    document.getElementById("Home").innerHTML = "";
    alert("Hello")
}