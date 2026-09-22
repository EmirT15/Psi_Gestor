from flask import Blueprint, jsonify, request

from services.auth_service import registrar_usuario, iniciar_sesion

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/auth/registro", methods=["POST"])
def registrar():
    datos = request.get_json()

    campos_requeridos = [
        "nombre",
        "apellido",
        "matricula",
        "correo",
        "password",
        "rol"
    ]

    for campo in campos_requeridos:
        if campo not in datos:
            return jsonify({
                "mensaje": f"El campo '{campo}' es obligatorio"
            }), 400

    for campo in campos_requeridos:
        if not str(datos[campo]).strip():
            return jsonify({
                "mensaje": f"El campo '{campo}' no puede estar vacío"
            }), 400

    
    usuario, error = registrar_usuario(
        datos["nombre"],
        datos["apellido"],
        datos["matricula"],
        datos["correo"],
        datos["password"],
        datos["rol"]
    )

    if error is not None:
        return jsonify({
            "mensaje": error
        }),     400

    return jsonify({
        "mensaje": "Usuario registrado correctamente",
        "usuario": {
            "id": usuario[0],
            "nombre": usuario[1],
            "apellido": usuario[2],
            "matricula": usuario[3],
            "correo": usuario[4],
            "rol": usuario[5]
        }
    }), 201


@auth_bp.route("/auth/login", methods=["POST"])
def login():
    datos = request.get_json()

    usuario = iniciar_sesion(
        datos["correo"],
        datos["password"]
    )

    if usuario is None:
        return jsonify({
            "mensaje": "Correo o contraseña incorrectos"
        }), 401

    return jsonify({
        "mensaje": "Inicio de sesión correcto",
        "usuario": {
            "id": usuario[0],
            "nombre": usuario[1],
            "apellido": usuario[2],
            "matricula": usuario[3],
            "correo": usuario[4],
            "rol": usuario[6]
        }
    }), 200