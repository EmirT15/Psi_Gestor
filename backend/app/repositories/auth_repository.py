import psycopg
import os


def crear_usuario(nombre, apellido, matricula, correo, password_hash, rol):
    conexion = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = conexion.cursor()

    try:
        cursor.execute("""
            INSERT INTO usuarios
            (nombre, apellido, matricula, correo, password_hash, rol)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id, nombre, apellido, matricula, correo, rol;
        """, (
            nombre,
            apellido,
            matricula,
            correo,
            password_hash,
            rol
        ))

        usuario = cursor.fetchone()

        conexion.commit()

        return usuario

    except psycopg.errors.UniqueViolation:
        conexion.rollback()
        return None

    finally:
        cursor.close()
        conexion.close()

def obtener_usuario_por_correo(correo):
    conexion = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, apellido, matricula, correo, password_hash, rol
        FROM usuarios
        WHERE correo = %s;
    """, (correo,))

    usuario = cursor.fetchone()

    cursor.close()
    conexion.close()

    return usuario