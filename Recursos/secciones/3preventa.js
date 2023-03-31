// Crea un array con los precios de cada fase

const precios = [0.0005, 0.00051, 0.00052, 0.00053, 0.00054, 0.00055, 0.00056, 0.00057, 0.00058, 0.0006];

// Obtiene todos los botones de compra

const botonesCompra = document.querySelectorAll('.comprar-btn');

// Itera sobre cada botón de compra y agrega un event listener

botonesCompra.forEach((boton, indice) => {

  boton.addEventListener('click', () => {

    // Obtiene el precio del botón actual utilizando el índice del botón en el array de precios

    const precio = precios[indice];

    // Aquí va el código para procesar la compra

    alert("Se ha comprado WLCV por " + precio + " BTCB");

  });

});
