import psycopg
import os

def obtener_estudiantes():
    conexion = psycopg.connect(
        host = os.getenv("DB_HOST"),
        port= os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")

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

def buscar_estudiantes_db(busqueda):
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
        FROM estudiantes
        WHERE
            nombre ILIKE %s OR
            apellido ILIKE %s OR
            matricula ILIKE %s OR
            carrera ILIKE %s
        ORDER BY id;
    """, (
        f"%{busqueda}%",
        f"%{busqueda}%",
        f"%{busqueda}%",
        f"%{busqueda}%"
    ))

    estudiantes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return estudiantes