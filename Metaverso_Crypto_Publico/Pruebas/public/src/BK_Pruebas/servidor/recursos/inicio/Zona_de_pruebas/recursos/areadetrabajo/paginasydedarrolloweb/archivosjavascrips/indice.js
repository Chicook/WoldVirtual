// Obtenemos los elementos que necesitamos
const links = document.querySelectorAll('nav a');
const content = document.querySelectorAll('.content');

// Agregamos un evento clic a cada enlace del menú
links.forEach((link, index) => {
  link.addEventListener('click', () => {
    // Quitamos la clase activa de todos los enlaces
    links.forEach(link => link.classList.remove('active'));
    // Agregamos la clase activa al enlace que se ha hecho clic
    link.classList.add('active');
    // Ocultamos todo el contenido y mostramos solo el contenido seleccionado
    content.forEach(item => item.style.display = 'none');
    content[index].style.display = 'block';
  });
});
