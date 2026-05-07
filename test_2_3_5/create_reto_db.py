"""Crea la base de datos reto_alvaro.db con la tabla LOGS
y añade 30 eventos inventados."""

import sqlite3
import os

DB_NAME = "reto_alvaro.db"

EVENTS = [
    "Inicio sistema",
    "Carga completa",
    "Usuario autenticado",
    "Usuario desconectado",
    "Error detectado",
    "Intento de reconexión",
    "Base de datos inicializada",
    "Backup automático",
    "Restauración completada",
    "Archivo subido",
    "Archivo eliminado",
    "Permiso denegado",
    "Permiso otorgado",
    "Actualización disponible",
    "Actualización aplicada",
    "Servicio iniciado",
    "Servicio detenido",
    "Latencia alta",
    "Tiempo de espera excedido",
    "Conexión establecida",
    "Conexión perdida",
    "Sesión expirada",
    "Nuevo registro creado",
    "Registro actualizado",
    "Registro eliminado",
    "Alerta crítica",
    "Advertencia de memoria",
    "Uso de CPU alto",
    "Tarea programada ejecutada",
    "Limpieza de recursos",
]


def create_db(path: str = DB_NAME) -> None:
    # Borra la base de datos si existe para crear una copia limpia
    if os.path.exists(path):
        os.remove(path)

    conn = sqlite3.connect(path)
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE LOGS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evento TEXT NOT NULL
        )
        """
    )

    # Inserta los eventos
    cur.executemany("INSERT INTO LOGS (evento) VALUES (?)", [(e,) for e in EVENTS])
    conn.commit()

    # Comprobación: contar filas
    cur.execute("SELECT COUNT(*) FROM LOGS")
    count = cur.fetchone()[0]

    print(f"Base de datos creada: {path}")
    print(f"Filas insertadas en LOGS: {count}")

    # Mostrar las primeras 5 filas como verificación
    cur.execute("SELECT id, evento FROM LOGS ORDER BY id LIMIT 5")
    rows = cur.fetchall()
    print("Primeras filas:")
    for r in rows:
        print(r)

    conn.close()


if __name__ == "__main__":
    create_db()