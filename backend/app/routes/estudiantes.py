from flask import Blueprint, jsonify, request
from services.estudiantes_service import (
    obtener_lista_estudiantes,
    crear_estudiante,
    actualizar_estudiante,
    eliminar_estudiante,
    buscar_estudiantes
)

estudiantes_bp = Blueprint("estudiantes", __name__)


@estudiantes_bp.route("/estudiantes", methods=["GET"])
def obtener_estudiantes():
    estudiantes = obtener_lista_estudiantes()

    return jsonify({
        "estudiantes": [
            {
                "id": estudiante[0],
                "nombre": estudiante[1],
                "apellido": estudiante[2],
                "matricula": estudiante[3],
                "carrera": estudiante[4],
                "semestre": estudiante[5],
                "correo": estudiante[6]
            }
            for estudiante in estudiantes
        ]
    })


@estudiantes_bp.route("/estudiantes/buscar", methods=["GET"])
def buscar_estudiantes_ruta():
    busqueda = request.args.get("q", "")

    estudiantes = buscar_estudiantes(busqueda)

    return jsonify({
        "estudiantes": [
            {
                "id": estudiante[0],
                "nombre": estudiante[1],
                "apellido": estudiante[2],
                "matricula": estudiante[3],
                "carrera": estudiante[4],
                "semestre": estudiante[5],
                "correo": estudiante[6]
            }
            for estudiante in estudiantes
        ]
    })


@estudiantes_bp.route("/estudiantes", methods=["POST"])
def crear_estudiante_ruta():
    datos = request.get_json()

    estudiante = crear_estudiante(
        datos["nombre"],
        datos["apellido"],
        datos["matricula"],
        datos["carrera"],
        datos["semestre"],
        datos["correo"]
    )

    return jsonify({
        "mensaje": "Estudiante creado correctamente",
        "estudiante": {
            "id": estudiante[0],
            "nombre": estudiante[1],
            "apellido": estudiante[2],
            "matricula": estudiante[3],
            "carrera": estudiante[4],
            "semestre": estudiante[5],
            "correo": estudiante[6]
        }
    }), 201


@estudiantes_bp.route("/estudiantes/<int:estudiante_id>", methods=["PUT"])
def actualizar_estudiante_ruta(estudiante_id):
    datos = request.get_json()

    estudiante = actualizar_estudiante(
        estudiante_id,
        datos["nombre"],
        datos["apellido"],
        datos["matricula"],
        datos["carrera"],
        datos["semestre"],
        datos["correo"]
    )

    if not estudiante:
        return jsonify({
            "mensaje": "Estudiante no encontrado"
        }), 404

    return jsonify({
        "mensaje": "Estudiante actualizado correctamente",
        "estudiante": {
            "id": estudiante[0],
            "nombre": estudiante[1],
            "apellido": estudiante[2],
            "matricula": estudiante[3],
            "carrera": estudiante[4],
            "semestre": estudiante[5],
            "correo": estudiante[6]
        }
    }), 200


@estudiantes_bp.route("/estudiantes/<int:id>", methods=["DELETE"])
def eliminar_estudiante_ruta(id):
    estudiante = eliminar_estudiante(id)

    if estudiante is None:
        return jsonify({
            "mensaje": "Estudiante no encontrado"
        }), 404

    return jsonify({
        "mensaje": "Estudiante eliminado correctamente",
        "estudiante": {
            "id": estudiante[0],
            "nombre": estudiante[1],
            "apellido": estudiante[2],
            "matricula": estudiante[3],
            "carrera": estudiante[4],
            "semestre": estudiante[5],
            "correo": estudiante[6]
        }
    }), 200