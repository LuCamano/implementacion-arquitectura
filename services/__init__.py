from models import *

class DepartamentoService:
    @staticmethod
    def create(**campos):
        departamento = Departamento(**campos)
        db.session.add(departamento)
        db.session.commit()
        return departamento
    
    @staticmethod
    def get_all():
        return Departamento.query.all()
    
    @staticmethod
    def get_by_pk(numero, idEdificio):
        return Departamento.query.get((numero, idEdificio))
    
    @staticmethod
    def update(numero, idEdificio, **campos):
        departamento = Departamento.query.get((numero, idEdificio))
        for key, value in campos.items():
            setattr(departamento, key, value)
        db.session.commit()
        return departamento

class EdificioService:
    @staticmethod
    def create(**campos):
        edificio = Edificio(**campos)
        db.session.add(edificio)
        db.session.commit()
        return edificio
    
    @staticmethod
    def get_all():
        return Edificio.query.all()
    
    @staticmethod
    def get_by_pk(idEdificio):
        return Edificio.query.get(idEdificio)
    
    @staticmethod
    def update(idEdificio, **campos):
        edificio = Edificio.query.get(idEdificio)
        for key, value in campos.items():
            setattr(edificio, key, value)
        db.session.commit()
        return edificio
    
class PagoService:
    @staticmethod
    def create(**campos):
        pago = Pago(**campos)
        db.session.add(pago)
        db.session.commit()
        return pago
    
    @staticmethod
    def get_all():
        return Pago.query.all()
    
    @staticmethod
    def get_by_pk(idPago):
        return Pago.query.get(idPago)
    
    @staticmethod
    def update(idGasto, numero, idEdificio, **campos):
        pago = Pago.query.get({idGasto, numero, idEdificio})
        for key, value in campos.items():
            setattr(pago, key, value)
        db.session.commit()
        return pago
    
class GastoService:
    @staticmethod
    def create(**campos):
        gasto = Gasto(**campos)
        db.session.add(gasto)
        db.session.commit()
        return gasto
    
    @staticmethod
    def get_all():
        return Gasto.query.all()
    
    @staticmethod
    def get_by_pk(idGasto):
        return Gasto.query.get(idGasto)
    
    @staticmethod
    def update(idGasto, **campos):
        gasto = Gasto.query.get(idGasto)
        for key, value in campos.items():
            setattr(gasto, key, value)
        db.session.commit()
        return gasto
    
class ServicioService:
    @staticmethod
    def create(**campos):
        servicio = Servicio(**campos)
        db.session.add(servicio)
        db.session.commit()
        return servicio
    
    @staticmethod
    def get_all():
        return Servicio.query.all()
    
    @staticmethod
    def get_by_pk(nombre):
        return Servicio.query.get(nombre)
    
    @staticmethod
    def update(nombre, **campos):
        servicio = Servicio.query.get(nombre)
        for key, value in campos.items():
            setattr(servicio, key, value)
        db.session.commit()
        return servicio