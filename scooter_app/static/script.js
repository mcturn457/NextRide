function showPassword() {
    var pw = document.getElementById("pw");
    if (pw.type === "password") {
        pw.type = "text";
    } else {
        pw.type = "password";
    }
}

export function getLocation(x) {
    if (navigator.geolocation) {
        var position = navigator.geolocation.getCurrentPosition();
        showPosition(position, x)
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

export function showPosition(position, x) {
x.innerHTML = "Latitude: " + position.coords.latitude + 
"<br>Longitude: " + position.coords.longitude;

var map = L.map('map').setView([position.coords.latitude, position.coords.longitude], 13);

var mode = document.getElementById('darkmode').textContent;

if (mode == "Dark Mode") {
    L.tileLayer('https://tile.jawg.io/jawg-light/{z}/{x}/{y}{r}.png?access-token=dzffigTwdQHUlNNFg0lfWIbJFJ5ohhOiViumMXwwZQNMgtUtyXiasK0bce9X8HsU', {}).addTo(map);
    map.attributionControl.addAttribution("<a href=\"https://www.jawg.io\" target=\"_blank\">&copy; Jawg</a> - <a href=\"https://www.openstreetmap.org\" target=\"_blank\">&copy; OpenStreetMap</a>&nbsp;contributors")
} else {
    L.tileLayer('https://tile.jawg.io/jawg-dark/{z}/{x}/{y}{r}.png?access-token=dzffigTwdQHUlNNFg0lfWIbJFJ5ohhOiViumMXwwZQNMgtUtyXiasK0bce9X8HsU', {}).addTo(map);
    map.attributionControl.addAttribution("<a href=\"https://www.jawg.io\" target=\"_blank\">&copy; Jawg</a> - <a href=\"https://www.openstreetmap.org\" target=\"_blank\">&copy; OpenStreetMap</a>&nbsp;contributors")

}
}


function darkMode() {
    var mode = document.getElementById("darkmode");

    if (mode.innerHTML == "Dark Mode") {
        document.body.style.backgroundColor = "#343541";
        document.body.style.color = "#ffffff";
        document.getElementById('darkmode').innerHTML = "Light Mode";
        getLocation(x);
    } else {
        document.body.style.backgroundColor = "#f2f2f2";
        document.body.style.color = "#000000";
        document.getElementById('darkmode').innerHTML = "Dark Mode";
        getLocation(x);
    }
}

function scooterAusleihen() {
    alert('Test');
}