import {Injectable, inject} from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { Estudiante, CrearEstudiante } from "../models/estudiante.model";

@Injectable({
    providedIn: 'root'
})
export class EstudiantesService {
    private http = inject(HttpClient);

private apiUrl = 'http://localhost:5000/estudiantes';

    obtenerEstudiantes(): Observable<{ estudiantes: Estudiante[]} > {
        return this.http.get<{estudiantes: Estudiante[] }> (this.apiUrl);
    }

    crearEstudiante(estudiante: CrearEstudiante): Observable<Estudiante> {
        return this.http.post<Estudiante>(this.apiUrl, estudiante);
    }

    eliminarEstudiante(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`);
    }
}