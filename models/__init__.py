from app import db
from datetime import datetime

class Empleado(db.Model):
    run = db.Column(db.String(12), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    sueldoHora = db.Column(db.Integer, nullable=False)
    horas = db.Column(db.Integer, nullable=False)
    contacto = db.Column(db.Integer, nullable=False)
    conEmergencia = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(15), nullable=False)

    def serialize(self):
        return {
            'run': self.run, 
            'nombre': self.nombre, 
            'sueldoHora': self.sueldoHora, 
            'horas': self.horas, 
            'contacto': self.contacto, 
            'conEmergencia': self.conEmergencia, 
            'tipo': self.tipo
        }
    
    def __repr__(self):
        return '<Empleado %r>' % self.run

class Edificio(db.Model):
    idEdificio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(30), nullable=False, unique=True)
    direccion = db.Column(db.String(35), nullable=False)
    numPisos = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'idEdificio': self.idEdificio, 
            'nombre': self.nombre, 
            'direccion': self.direccion, 
            'numPisos': self.numPisos
        }
    
    def __repr__(self):
        return '<Edificio %r>' % self.idEdificio
    
class EmpleadoEdificio(db.Model):
    idEmpleadoEdificio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    run = db.Column(db.String(12), db.ForeignKey('empleado.run'), nullable=False)
    idEdificio = db.Column(db.Integer, db.ForeignKey('edificio.idEdificio'), nullable=False)
    inicio = db.Column(db.Date, nullable=False)
    termino = db.Column(db.Date, nullable=True)

    def serialize(self):
        return {
            'run': self.run, 
            'idEdificio': self.idEdificio, 
            'inicio': self.inicio, 
            'termino': self.termino
        }
    
    def __repr__(self):
        return '<EmpleadoEdificio %r>' % self.idEmpleadoEdificio
    
class Departamento(db.Model):
    idDepartamento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero = db.Column(db.Integer, nullable=False)
    piso = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(10), nullable=False)
    idEdificio = db.Column(db.Integer, db.ForeignKey('edificio.idEdificio'), nullable=False)

    def serialize(self):
        return {
            'numero': self.numero, 
            'piso': self.piso, 
            'estado': self.estado, 
            'idEdificio': self.idEdificio
        }
    
    def __repr__(self):
        return '<Departamento %r>' % self.numero

class Solicitud(db.Model):
    idSolicitud = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    idDepartamento = db.Column(db.Integer, db.ForeignKey('departamento.idDepartamento'), nullable=False)
    
    def serialize(self):
        return {
            'idSolicitud': self.idSolicitud, 
            'tipo': self.tipo, 
            'descripcion': self.descripcion, 
            'fecha': self.fecha, 
            'numero': self.numero, 
            'idEdificio': self.idEdificio
        }
    
    def __repr__(self):
        return '<Solicitud %r>' % self.idSolicitud
class Gasto(db.Model):
    idGasto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(15), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    idDepartamento = db.Column(db.Integer, db.ForeignKey('departamento.idDepartamento'), nullable=False)

    def serialize(self):
        return {
            'idGasto': self.idGasto, 
            'valor': self.valor, 
            'tipo': self.tipo, 
            'descripcion': self.descripcion, 
            'estado': self.estado, 
            'fecha': self.fecha
        }
    
    def __repr__(self):
        return '<Gasto %r>' % self.idGasto
class Pago(db.Model):
    idPago = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idGasto = db.Column(db.Integer, db.ForeignKey('gasto.idGasto'), nullable=False)
    montoPagado = db.Column(db.Integer, nullable=False)
    fechaPago = db.Column(db.Date, nullable=False, default=datetime.now())

    def serialize(self):
        return {
            'idGasto': self.idGasto, 
            'numero': self.numero, 
            'idEdificio': self.idEdificio, 
            'montoPagado': self.montoPagado, 
            'fechaPago': self.fechaPago
        }

class Servicio(db.Model):
    nombre = db.Column(db.String(25), primary_key=True, nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    idGasto = db.Column(db.Integer, db.ForeignKey('gasto.idGasto'), nullable=False)

    def serialize(self):
        return {
            'nombre': self.nombre, 
            'descripcion': self.descripcion, 
            'idGasto': self.idGasto
        }
class Persona(db.Model):
    run = db.Column(db.String(12), primary_key=True, nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    contacto = db.Column(db.Integer, nullable=False)
    conEmergencia = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'run': self.run, 
            'nombre': self.nombre, 
            'apellido': self.apellido, 
            'contacto': self.contacto, 
            'conEmergencia': self.conEmergencia
        }

class Residente(db.Model):
    idResidente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    run = db.Column(db.String(12), db.ForeignKey('persona.run'), nullable=False)
    idDepartamento = db.Column(db.Integer, db.ForeignKey('departamento.idDepartamento'), nullable=False)
    inicio = db.Column(db.Date, nullable=False)
    termino = db.Column(db.Date, nullable=True)

    def serialize(self):
        return {
            'run': self.run, 
            'numero': self.numero, 
            'idEdificio': self.idEdificio, 
            'inicio': self.inicio, 
            'termino': self.termino
        }

class Propietario(db.Model):
    idPropietario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    run = db.Column(db.String(12), db.ForeignKey('persona.run'), nullable=False)
    idDepartamento = db.Column(db.Integer, db.ForeignKey('departamento.idDepartamento'), nullable=False)
    inicio = db.Column(db.Date, nullable=False)
    termino = db.Column(db.Date, nullable=True)

    def serialize(self):
        return {
            'run': self.run, 
            'numero': self.numero, 
            'idEdificio': self.idEdificio, 
            'inicio': self.inicio, 
            'termino': self.termino
        }
