var myVar = setInterval(myTimer, 1000);

function myTimer() {
    var d = new Date();
    document.getElementById("time").innerHTML = d.toLocaleTimeString();
}