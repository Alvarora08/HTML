# Importamos la función para manejar plantillas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/coleccion")
def ver_coleccion():
    # Creamos una lista de diccionarios con datos de prueba
    mis_favs = [
        {"nombre": "Tenis", "motivo": "la intensidad del juego"},
        {"nombre": "Ciclismo de montaña", "motivo": "sentir la adrelanina de las bajadas"},
        {"nombre": "Estar en el sofa", "motivo": "no tener que hacer nada"}
    ]
    # Enviamos la lista completa a la plantilla con el nombre 'items'
    return render_template("index_2_3_4.html", favs=mis_favs)

if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)