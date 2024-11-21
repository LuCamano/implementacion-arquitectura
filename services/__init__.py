from datetime import datetime
from models import *
from app import db

# Clase base para los servicios
class BaseService:
    _model: type = None
    
    @classmethod
    def create(cls,**campos):
        obj = cls._model(**campos)
        db.session.add(obj)
        db.session.commit()
        return obj
    
    @classmethod
    def get_all(cls):
        return cls._model.query.all()
    
    @classmethod
    def get_by_pk(cls, pk):
        primary_key_column = cls._model.__mapper__.primary_key[0]
        return cls._model.query.filter(primary_key_column == pk).first()
    
    @classmethod
    def update(cls, pk, **campos):
        obj = cls.get_by_pk(pk)
        for key, value in campos.items():
            setattr(obj, key, value)
        db.session.commit()
        return obj
    
    @classmethod
    def delete(cls, pk):
        obj = cls._model.query.get(pk)
        db.session.delete(obj)
        db.session.commit()
        return obj
    
    @classmethod
    def filter_by(cls, **kwargs):
        return cls._model.query.filter_by(**kwargs).all()

class DepartamentoService(BaseService):
    _model = Departamento
    
    @classmethod
    def get_by_edificio(cls, idEdificio):
        return cls.filter_by(idEdificio=idEdificio)
    

class EdificioService(BaseService):
    
    _model = Edificio
    

class PagoService(BaseService):
    
    _model = Pago
    
class GastoService(BaseService):
    
    _model = Gasto
    
    @classmethod
    def create(cls, **campos):
        strFecha = campos.get('fecha')
        if strFecha:
            campos['fecha'] = datetime.strptime(strFecha, '%d-%m-%Y')
        return super().create(**campos)
    
    @classmethod
    def get_by_departamento(cls, idDepartamento):
        return cls.filter_by(idDepartamento=idDepartamento)
    
    @classmethod
    def hacer_pago(cls, idGasto, monto):
        gasto = cls.get_by_pk(idGasto)
        pagos = PagoService.filter_by(idGasto=idGasto)
        total_pagado = sum([p.montoPagado for p in pagos])
        por_pagar = gasto.valor - total_pagado
        
        if por_pagar <= 0:
            raise Exception('El gasto ya fue pagado')
        if monto > por_pagar:
            raise Exception('El monto a pagar excede lo que se debe')\
        
        nuevoPago = PagoService.create(idGasto=idGasto, montoPagado=monto)
        pagos.append(nuevoPago)
        return gasto, pagos

class ServicioService(BaseService):
    
    _model = Servicio