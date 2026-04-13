//ai
function pos() {
    const boat_heading = parseFloat(document.getElementById("heading").value);
if (isNaN(boat_heading)){
        document.getElementById('output').innerText = "Please enter valid numbers.";
        return;}
    fetch('http://127.0.0.1:5000/api/pos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({boat_heading: boat_heading})
    })
    .then(response => response.json())
    .then(data => {
        const output = document.getElementById('output');
        // Basic HTML: point + list
        output.innerHTML = `<strong>Point of Sail:</strong> ${data.point}<br><strong>Advice:</strong><ul>` +
            data.advice.map(item => `<li>${item}</li>`).join('') +
            `</ul>`;
    })
    .catch(() => {
        document.getElementById('output').innerText = "Something went wrong. Try again.";
    });
}
//ai ends


function upwind() {
    const direction = document.getElementById("direction").value;

    document.getElementById("direction").value = "";
    document.getElementById("direction").focus();

    fetch('http://127.0.0.1:5000/api/upwind', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ move_input: direction })
    })
    .then(res => res.json())
    .then(data => {
        const output = document.getElementById("mapOutput");

        output.innerHTML = "<pre>" + data.map.join("\n") + "</pre>";
    });
}
// initial board load, created with help from ai
function loadBoard() {
    fetch('http://127.0.0.1:5000/api/upwind', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ move_input: "" })
    })
    .then(res => res.json())
    .then(data => {
        const output = document.getElementById("mapOutput");
        output.innerHTML = "<pre>" + data.map.join("\n") + "</pre>";
    });
}

document.addEventListener('DOMContentLoaded', function() {
    loadBoard();

    // Add Enter key support for direction input
    document.getElementById('direction').addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            upwind();
        }
    });
});
