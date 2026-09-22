from werkzeug.security import generate_password_hash, check_password_hash

from repositories.auth_repository import crear_usuario, obtener_usuario_por_correo


def registrar_usuario(nombre, apellido, matricula, correo, password, rol):

    if rol not in ["estudiante", "psicologo"]:
        return None, "Rol no válido"

    password_hash = generate_password_hash(password)

    usuario = crear_usuario(
        nombre,
        apellido,
        matricula,
        correo,
        password_hash,
        rol
    )
    if usuario is None:
        return None, "La matrícula o el correo ya están registrados"

    return usuario, None

def iniciar_sesion(correo, password):
    usuario = obtener_usuario_por_correo(correo)

    if usuario is None:
        return None

    password_correcta = check_password_hash(
        usuario[5],
        password
    )

    if not password_correcta:
        return None

    return usuario