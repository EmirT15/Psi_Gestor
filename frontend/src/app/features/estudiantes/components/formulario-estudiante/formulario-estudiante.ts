import { Component, EventEmitter, inject, Input, OnChanges, Output, SimpleChanges } from '@angular/core';
import { Button } from '../../../../shared/components/button/button';
import { FormsModule } from '@angular/forms';
import { EstudiantesService } from '../../services/estudiantes.service';
import { CrearEstudiante, Estudiante } from '../../models/estudiante.model';

@Component({
  selector: 'app-formulario-estudiante',
  standalone: true,
  imports: [Button, FormsModule],
  templateUrl: './formulario-estudiante.html',
  styleUrl: './formulario-estudiante.css'
})
export class FormularioEstudiante implements OnChanges {
  @Input() estudianteEditar: Estudiante | null = null;

  nombre: string = '';
  apellido: string = '';
  matricula: string = '';
  carrera: string = '';
  semestre: number = 0;
  correo: string = '';
  private estudiantesService = inject(EstudiantesService);
  @Output() estudianteGuardado = new EventEmitter<void>();

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['estudianteEditar'] && this.estudianteEditar) {
      this.nombre = this.estudianteEditar.nombre;
      this.apellido = this.estudianteEditar.apellido;
      this.matricula = this.estudianteEditar.matricula;
      this.carrera = this.estudianteEditar.carrera;
      this.semestre = this.estudianteEditar.semestre;
      this.correo = this.estudianteEditar.correo;
    }
  }

  guardarEstudiante(): void {
    const estudianteData: CrearEstudiante = {
      nombre: this.nombre,
      apellido: this.apellido,
      matricula: this.matricula,
      carrera: this.carrera,
      semestre: this.semestre,
      correo: this.correo
    };

    if (this.estudianteEditar) {
      // Modo Edición
      this.estudiantesService.actualizarEstudiante(this.estudianteEditar.id, estudianteData).subscribe({
        next: (respuesta) => {
          console.log('Estudiante actualizado:', respuesta);
          this.estudianteGuardado.emit();
        },
        error: (error) => console.error('Error al actualizar estudiante:', error)
      });
    } else {
      // Modo Creación
      this.estudiantesService.crearEstudiante(estudianteData).subscribe({
        next: (respuesta) => {
          console.log('Estudiante creado:', respuesta);
          this.estudianteGuardado.emit();
        },
        error: (error) => console.error('Error al crear estudiante:', error)
      });
    }
  }


}