import { Component, EventEmitter, inject, Output } from '@angular/core';
import { Button } from '../../../../shared/components/button/button';
import { FormsModule } from '@angular/forms';
import { EstudiantesService } from '../../services/estudiantes.service';
import { CrearEstudiante } from '../../models/estudiante.model';

@Component({
  selector: 'app-formulario-estudiante',
  standalone: true,
  imports: [Button, FormsModule],
  templateUrl: './formulario-estudiante.html',
  styleUrl: './formulario-estudiante.css'
})
export class FormularioEstudiante {

  nombre: string = '';
  apellido: string = '';
  matricula: string = '';
  carrera: string = '';
  semestre: number = 0;
  correo: string = '';
  private estudiantesService = inject(EstudiantesService);
  @Output() estudianteCreado = new EventEmitter<void>();

  guardarEstudiante(): void {
  const estudiante: CrearEstudiante = {
    nombre: this.nombre,
    apellido: this.apellido,
    matricula: this.matricula,
    carrera: this.carrera,
    semestre: this.semestre,
    correo: this.correo
  };

  this.estudiantesService.crearEstudiante(estudiante).subscribe({
    next: (respuesta) => {
      console.log('Estudiante creado:', respuesta);
      this.estudianteCreado.emit();

    },
    error: (error) => {
      console.error('Error al crear estudiante:', error);
    }
  });
}


}