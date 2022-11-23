document.addEventListener("DOMContentLoaded", function (event) {
  //código a ejecutar cuando el DOM está listo para recibir acciones
  var alertElem
  alertElem = document.getElementById('alerts')
  if (typeof (alertElem) != 'undefined' && alertElem != null) {
    alertElem.style.display = 'block';
    alertElem.classList.remove('height');
    setTimeout(() => {
      alertElem.style.display = 'none';
  }, 2500);

  }
  
  const checkbox = document.getElementById('checkbox');

  const is_dark = localStorage.getItem('dark-theme');
  if (is_dark === 'true') {
    if (!document.body.classList.contains('dark')) {
      document.body.classList.add('dark');
    }
  } else {
    if (document.body.classList.contains('dark')) {
      document.body.classList.remove('dark');
    }
  }

  checkbox.addEventListener('change', () => {
    document.body.classList.toggle('dark');
    if (document.body.classList.contains('dark')) {
      localStorage.setItem('dark-theme', 'true')
    } else {
      localStorage.setItem('dark-theme', 'false')
    }
    
  })

});

