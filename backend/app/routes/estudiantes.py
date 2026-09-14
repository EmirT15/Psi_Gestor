from flask import Blueprint, jsonify, request
from services.estudiantes_service import obtener_lista_estudiantes, crear_estudiante

estudiantes_bp = Blueprint("estudiantes",__name__)

@estudiantes_bp.route("/estudiantes", methods=["Get"])
def obtener_estudiantes():
    estudiantes = obtener_lista_estudiantes()

    return jsonify({
        "estudiantes": 
        [
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