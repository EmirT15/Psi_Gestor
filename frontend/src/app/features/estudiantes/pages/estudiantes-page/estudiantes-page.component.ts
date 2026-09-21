import { Component, OnInit, inject, signal } from '@angular/core';
import { EstudiantesService } from '../../services/estudiantes.service';
import { Estudiante } from '../../models/estudiante.model';
import { Button } from '../../../../shared/components/button/button';
import { FormularioEstudiante } from '../../components/formulario-estudiante/formulario-estudiante';

@Component({
    selector: 'app-estudiantes-page',
    standalone: true,
    imports: [Button, FormularioEstudiante],
    templateUrl: './estudiantes-page.component.html',
    styleUrl: './estudiantes-page.component.css'
})

export class EstudiantesPageComponent implements OnInit {
    private estudiantesService = inject(EstudiantesService);

    estudiantes = signal<Estudiante[]>([]);

    mostrarFormulario: boolean = false;

    estudianteSeleccionado: Estudiante | null = null;

    ngOnInit(): void {
        this.cargarEstudiantes();
    }

    cargarEstudiantes(): void {
        this.estudiantesService.obtenerEstudiantes().subscribe({
            next: (respuesta) => {
                console.log('Estudiantes recibidos:', respuesta);
                this.estudiantes.set(respuesta.estudiantes);
            },
            error: (error) => {
                console.error("error al obtener estudiantes", error);
            }
        });
    }

    seleccionarParaEditar(estudiante: Estudiante): void {
        this.estudianteSeleccionado = estudiante;
        this.mostrarFormulario = true;
    }

    abrirFormularioNuevo(): void {
        this.estudianteSeleccionado = null;
        this.mostrarFormulario = !this.mostrarFormulario;
    }

    finalizarGuardado(): void {
        this.mostrarFormulario = false;
        this.estudianteSeleccionado = null;
        this.cargarEstudiantes();
    }
}