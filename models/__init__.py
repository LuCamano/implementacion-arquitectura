from app import db

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
    idEdificio = db.Column(db.Integer, primary_key=True)
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
    run = db.Column(db.String(12), db.ForeignKey('empleado.run'), nullable=False)
    idEdificio = db.Column(db.Integer, db.ForeignKey('edificio.idEdificio'), nullable=False)
    inicio = db.Column(db.Date, nullable=False)
    termino = db.Column(db.Date, nullable=True)

    __table_args__ = (
        db.PrimaryKeyConstraint('run', 'idEdificio'),
    )

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
    numero = db.Column(db.Integer, nullable=False)
    piso = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.String(10), nullable=False)
    idEdificio = db.Column(db.Integer, db.ForeignKey('edificio.idEdificio'), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('numero', 'idEdificio'),
    )

    def serialize(self):
        return {
            'numero': self.numero, 
            'piso': self.piso, 
            'estado': self.estado, 
            'idEdificio': self.idEdificio
        }
