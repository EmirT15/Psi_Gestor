export interface Estudiante {
  id: number;
  nombre: string;
  apellido: string;
  matricula: string;
  carrera: string;
  semestre: number;
  correo: string;
}

export interface CrearEstudiante {
  nombre: string;
  apellido: string;
  matricula: string;
  carrera: string;
  semestre: number;
  correo: string;
}