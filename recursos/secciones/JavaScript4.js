// Obtener elementos de la página
const toggleBtn = document.querySelector('#toggleBtn');
const nav = document.querySelector('nav');
const sections = document.querySelectorAll('section');
const accBtns = document.querySelectorAll('.accordion-btn');

// Agregar evento de clic para el botón de alternancia del menú
toggleBtn.addEventListener('click', function() {
    nav.classList.toggle('show');
});

// Agregar eventos de clic para los botones de acordeón
accBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        const panel = this.nextElementSibling;
        panel.classList.toggle('show');
    });
});

// Agregar efecto de desplazamiento suave a los enlaces de anclaje
const smoothScroll = function(target, duration) {
    const targetPos = target.getBoundingClientRect().top + window.pageYOffset;
    const startPos = window.pageYOffset;
    const distance = targetPos - startPos;
    let startTime = null;

    const animation = function(currentTime) {
        if (startTime === null) {
            startTime = currentTime;
        }
        const timeElapsed = currentTime - startTime;
        const run = ease(timeElapsed, startPos, distance, duration);
        window.scrollTo(0, run);
        if (timeElapsed < duration) {
            requestAnimationFrame(animation);
        }
    };

    const ease = function(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
    };

    requestAnimationFrame(animation);
};

const links = document.querySelectorAll('a[href^="#"]');
links.forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        const duration = 1000;
        smoothScroll(target, duration);
    });
});
