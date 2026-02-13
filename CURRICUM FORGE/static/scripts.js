function getMessage() {
    fetch("/hello")
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText = data.message;
    });
}