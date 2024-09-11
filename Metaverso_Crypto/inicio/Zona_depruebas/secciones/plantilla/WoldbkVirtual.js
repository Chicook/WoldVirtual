// script.js
// plataforma  principal.
function enviarMensaje() {
    var mensajeInput = document.getElementById('mensajeInput');
    var mensaje = mensajeInput.value.trim();

    if (mensaje !== '') {
        var chatDiv = document.getElementById('chat');
        var nuevoMensaje = document.createElement('div');
        nuevoMensaje.className = 'mensaje';
        nuevoMensaje.textContent = mensaje;
        chatDiv.appendChild(nuevoMensaje);
        mensajeInput.value = '';

        // Desvanecer después de 5 segundos
        setTimeout(function() {
            nuevoMensaje.style.opacity = '0';
            setTimeout(function() {
                nuevoMensaje.style.display = 'none';
            }, 1000); // Retraso adicional para permitir que termine la transición
        }, 5000);
    }
}