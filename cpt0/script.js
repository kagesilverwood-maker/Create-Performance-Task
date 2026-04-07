function pos() {
    const wind_speed = parseInt(document.getElementById("wind").value);
    const boat_heading = parseFloat(document.getElementById("heading").value);
if (isNaN(wind_speed) || isNaN(boat_heading)){
        document.getElementById('output').innerText = "Please enter valid numbers.";
        return;}
    fetch('http://127.0.0.1:5000/api/pos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            wind_speed: wind_speed,
            boat_heading: boat_heading
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output').innerText =
            "Point of Sail: " + data.point + "\n" +
            "Advice: " + data.advice;
    });
}