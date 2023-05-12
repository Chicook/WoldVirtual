const loanButton = document.querySelector('.loan-button');
const loanConditions = document.querySelector('.loan-conditions');

loanButton.addEventListener('click', () => {
  loanConditions.style.display = 'block';
});
