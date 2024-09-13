function calcularComision() {

  let moneda_envio = document.getElementById("moneda_envio").value;

  let moneda_recepcion = document.getElementById("moneda_recepcion").value;

  let monto_envio = document.getElementById("monto_envio").value;

  let comision = 0.001;

  let conversion_rate = obtenerConversion(moneda_recepcion);

  let comision_equivalente = comision * conversion_rate;

  let mensaje = `La comisión es de ${comision} WLCV, equivalente a ${comision_equivalente.toFixed(8)} ${moneda_recepcion}`;

  alert(mensaje);

}

function obtenerConversion(moneda_recepcion) {

  //Aquí se colocaría la lógica para obtener la tasa de conversión de la moneda de recepción

  //en relación a WLCV, usando alguna API o base de datos externa.

  //En este ejemplo, simplemente se devuelve una tasa de conversión aleatoria entre 0 y 1.

  return Math.random();

}
