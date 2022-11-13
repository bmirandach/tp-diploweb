document.addEventListener("DOMContentLoaded", function (event) {
  //código a ejecutar cuando el DOM está listo para recibir acciones
  var alertElem
  alertElem = document.getElementById('alerts')
  if (typeof (alertElem) != 'undefined' && alertElem != null) {
    alertElem.style.display = 'block';
    alertElem.classList.remove('height');
    setTimeout(() => {
      alertElem.style.display = 'none';
  }, 3000);

  }
  

});