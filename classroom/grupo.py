from asignatura import Asignatura
class Grupo:

    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        self.grado = "Grado 12"
    def __str__(self):
        cadena = "Grupo de estudiantes: " + self._grupo
        return cadena

    def listadoAsignaturas(self, **kwargs):
        L = []
        for x in kwargs:
            L.append(x)
        self._asignaturas = L

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista=[]
        lista.append(alumno)
        self.listadoAlumnos = lista
        return list

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

