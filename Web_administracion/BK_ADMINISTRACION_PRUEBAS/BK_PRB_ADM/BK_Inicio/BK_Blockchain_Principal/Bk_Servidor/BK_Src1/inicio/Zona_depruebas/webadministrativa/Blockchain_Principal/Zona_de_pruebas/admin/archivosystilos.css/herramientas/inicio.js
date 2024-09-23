// Obtener los enlaces de la página

const enlaces = document.querySelectorAll("a");

// Agregar un evento clic a cada enlace

enlaces.forEach((enlace) => {

  enlace.addEventListener("click", (evento) => {

    // Prevenir la acción predeterminada del enlace

    evento.preventDefault();

    // Obtener el href del enlace

    const href = enlace.getAttribute("href");

    // Desplazarse suavemente a la sección correspondiente

    document.querySelector(href).scrollIntoView({

      behavior: "smooth",

    });

  });

});
