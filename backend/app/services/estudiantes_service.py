from repositories.estudiantes_repository import obtener_estudiantes, crear_estudiante_db


def obtener_lista_estudiantes():
    return obtener_estudiantes()


def crear_estudiante(nombre, apellido, matricula, carrera, semestre, correo):
    return crear_estudiante_db(
        nombre,
        apellido,
        matricula,
        carrera,
        semestre,
        correo
    )

from repositories.estudiantes_repository import (
    obtener_estudiantes, 
    crear_estudiante_db,
    actualizar_estudiante_db  # <--- Agregado
)


def obtener_lista_estudiantes():
    return obtener_estudiantes()


def crear_estudiante(nombre, apellido, matricula, carrera, semestre, correo):
    return crear_estudiante_db(
        nombre,
        apellido,
        matricula,
        carrera,
        semestre,
        correo
    )


def actualizar_estudiante(estudiante_id, nombre, apellido, matricula, carrera, semestre, correo):
    return actualizar_estudiante_db(
        estudiante_id,
        nombre,
        apellido,
        matricula,
        carrera,
        semestre,
        correo
    )