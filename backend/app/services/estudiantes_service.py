from repositories.estudiantes_repository import (
    obtener_estudiantes,
    crear_estudiante_db,
    actualizar_estudiante_db,
    eliminar_estudiante_db,
    buscar_estudiantes_db
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


def eliminar_estudiante(id):
    return eliminar_estudiante_db(id)


def buscar_estudiantes(busqueda):
    return buscar_estudiantes_db(busqueda)