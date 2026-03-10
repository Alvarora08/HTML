const boton = document.getElementById("botón");
const parrafo = document.getElementById("estado");

// Cambiar ánimo al hacer clic
boton.addEventListener("click", function () {
    parrafo.textContent = "¡Día fantástico para Álvaro!";
    parrafo.style.color = "orange";
});

// Cambiar texto y tamaño al pasar el ratón
boton.addEventListener("mouseenter", function () {
    boton.textContent = "¡Púlsame, Rodríguez!";
    boton.style.fontSize = "18px";
});