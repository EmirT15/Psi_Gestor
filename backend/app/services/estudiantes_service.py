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