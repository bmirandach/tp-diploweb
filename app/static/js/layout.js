/*--------------------------------------*/
/* muestra/oculta submenu del nav       */
/*--------------------------------------*/
let subMenu = document.getElementById("subMenu");

function toggleMenu()
{
    subMenu.classList.toggle("open-menu");
}

document.addEventListener("DOMContentLoaded", function (event) {
  //código a ejecutar cuando el DOM está listo para recibir acciones

  /*--------------------------------------*/
  /* muestra la alerta por 2.5 seg        */
  /*--------------------------------------*/
  const alertElem = document.getElementById('alerts')
  if (typeof (alertElem) != 'undefined' && alertElem != null) {
    alertElem.style.display = 'block'
    alertElem.classList.remove('height')
    setTimeout(() => {
      alertElem.style.display = 'none'
    }, 2500);
  }
  
  /*----------------------------------------------*/
  /* aplica/quita el tema oscuro y guarda el dato */
  /*----------------------------------------------*/
  const checkbox = document.getElementById('checkbox')
  const is_dark = localStorage.getItem('dark-theme')
  if (is_dark === 'true') {
    if (!document.body.classList.contains('dark')) {
      document.body.classList.add('dark')
    }
  } else {
    if (document.body.classList.contains('dark')) {
      document.body.classList.remove('dark')
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

  /*--------------------------------------*/
  /* menu mobile y pequeñas pantallas     */
  /*--------------------------------------*/
  const symmenu = document.getElementById('navbar__toggle')
  const menu = document.getElementById('navbar__menu')
  symmenu.addEventListener('click', function () {
    menu.classList.toggle('navbar__menu--open')
    this.classList.toggle('navbar__toggle--open')
  })

});