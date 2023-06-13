class Persona:
    def _init_(self,paramNombre,paramApellido,paramEmail,paramTelefono,paramDireccion):
        self.nombre = paramNombre
        self.apellido = paramApellido
        self.email = paramEmail
        self.telefono = paramTelefono
        self.direccion = paramDireccion

class Profesor(Persona):
    def _init_(self,paramProfLegajo,paramNombre,paramApellido,paramEmail,paramTelefono,paramDireccion):
        self.idProf = paramProfLegajo
        super()._init_(paramNombre,paramApellido,paramEmail,paramTelefono,paramDireccion)

profesorDanielQuinteros = Profesor(45232,"Daniel","Quinteros","Daniel@um.edu.ar","261.343.2543","Godoy Cruz")
profesorDarioReynoso = Profesor(56434,"Dario","REynoso","d.reynoso@um.edu.ar","261.543.6532","Palmira")

class Alumno(Persona):
    def _init_ (self,paramLegajo,paramNombre,paramApellido,paramEmail,paramTelefono,paramDireccion):
        self.legajo = paramLegajo
        super()._init_(paramNombre,paramApellido,paramEmail,paramTelefono,paramDireccion)

alumnoValentinBecerra = Alumno("Valentin","Becerra","v.becerra@alumno.um.edu.ar",59177,"261.302.5653","Altezana")
alumnoSamuelLaucha = Alumno("Samuel","Laucha","Laucha@Samu.um.edu.ar",59234,"2616666666","Michigan")

class Materia:
    def _init_(self,paramIdMat,paramNombreMat,paramHorario,paramPeriodo):
        self.idMat = paramIdMat
        self.nombreMat = paramNombreMat
        self.horarioMat = paramHorario
        self.periodoMat = paramPeriodo

materiaComputacion = Materia(4567,"Computacion","Martes de 8:00 a 12:00","Anual")
materiaCalculoI = Materia(4890,"Calculo I","Lunes de 15:00 a 18:00","Semestral")


if __name__ == "__main__":
    pass