// Obtener el pop-up y el enlace de los términos y condiciones
  const popup = document.getElementById("popup");
  const link = document.querySelector(".terms");
  
  // Obtener el botón "cerrar" del pop-up
  const closeBtn = popup.querySelector(".close");
  
  // Mostrar el pop-up al hacer clic en el enlace
  link.addEventListener("click", function() {
    popup.style.display = "block";
  });
  
  // Ocultar el pop-up al hacer clic en el botón "cerrar"
  closeBtn.addEventListener("click", function() {
    popup.style.display = "none";
  });
  
  // Ocultar el pop-up al hacer clic fuera del mismo
  window.addEventListener("click", function(event) {
    if (event.target == popup) {
      popup.style.display = "none";
    }
  });
  