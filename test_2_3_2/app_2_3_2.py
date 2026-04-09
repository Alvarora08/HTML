# Importamos la función para manejar plantillas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    # Buscamos el archivo 'index.html' dentro de la carpeta /templates
    # También podemos pasar datos como variables (nombre="Alvaro")
    return render_template("perfil_2_3_2.html", estudiante="Álvaro Rodríguez Andrades", nickname= "Álvaro", id_dev="4567")

# Comprobamos si el script se está ejecutando directamente (y no importado como módulo)
if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)
