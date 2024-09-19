// Permette il drop
function allowDrop(event) {
    event.preventDefault();
}

// Dragging l'elemento
function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
}

// Dropping l'elemento nell'area corretta
function drop(event) {
    event.preventDefault();
    var data = event.dataTransfer.getData("text");
    var token = document.getElementById(data);
    event.target.appendChild(token);
    
    // Messaggio di successo
    alert("Hai spostato il gettone " + token.innerText + " correttamente!");
}
