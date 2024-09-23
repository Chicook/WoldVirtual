document.addEventListener('DOMContentLoaded', function() {
  const links = document.querySelectorAll('a');

  links.forEach(link => {
    link.addEventListener('click', function(event) {
      event.preventDefault();
      alert(`You clicked on ${this.textContent}`);
    });
  });
});
