
import psycopg
import os


def obtener_estudiantes():

    conexion = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, apellido, matricula, carrera, semestre, correo
        FROM estudiantes;
    """)

    estudiantes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return estudiantes


def crear_estudiante_db(nombre, apellido, matricula, carrera, semestre, correo):

    conexion = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO estudiantes
        (nombre, apellido, matricula, carrera, semestre, correo)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id, nombre, apellido, matricula, carrera, semestre, correo;
    """, (
        nombre,
        apellido,
        matricula,
        carrera,
        semestre,
        correo
    ))

    estudiante = cursor.fetchone()

    conexion.commit()
    cursor.close()
    conexion.close()

    return estudiante


def actualizar_estudiante_db(estudiante_id, nombre, apellido, matricula, carrera, semestre, correo):

    conexion = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE estudiantes
        SET nombre = %s,
            apellido = %s,
            matricula = %s,
            carrera = %s,
            semestre = %s,
            correo = %s
        WHERE id = %s
        RETURNING id, nombre, apellido, matricula, carrera, semestre, correo;
    """, (
        nombre,
        apellido,
        matricula,
        carrera,
        semestre,
        correo,
        estudiante_id
    ))

    estudiante = cursor.fetchone()

    conexion.commit()
    cursor.close()
    conexion.close()

    return estudiante


def eliminar_estudiante_db(id):

    conexion = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM estudiantes
        WHERE id = %s
        RETURNING id, nombre, apellido, matricula, carrera, semestre, correo;
    """, (id,))

    estudiante = cursor.fetchone()

    conexion.commit()
    cursor.close()
    conexion.close()

    return estudiante