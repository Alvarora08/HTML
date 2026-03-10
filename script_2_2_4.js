const boton = document.querySelector("#btn-modo");

boton.addEventListener("click", function () {
    // Alterna la clase 'noche' en todo el cuerpo de la web
    document.body.classList.toggle("noche");
});