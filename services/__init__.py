from datetime import datetime

from sqlalchemy import extract
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
    def filter_by_date(cls, year:int, mm:int=None, dd:int=None):
        query = cls._model.query.filter(
            extract('year', cls._model.fecha) == year
        )
        if mm is not None:
            query = query.filter(extract('month', cls._model.fecha) == mm)
        if dd is not None:
            query = query.filter(extract('day', cls._model.fecha) == dd)
        gastos = query.all()
        return gastos

    @classmethod
    def get_by_departamento(cls, idDepartamento, estado=None):
        if estado:
            return cls.filter_by(idDepartamento=idDepartamento, estado=estado)
        else:
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
            raise Exception('El monto a pagar excede lo que se debe')
        
        total_pagado += monto
        por_pagar -= monto
        
        nuevoPago = PagoService.create(idGasto=idGasto, montoPagado=monto)
        if total_pagado == gasto.valor:
            gasto.estado = 'pagado'
        pagos.append(nuevoPago)
        return gasto, pagos, por_pagar, total_pagado
    
    @classmethod
    def generar_gastos_comunes(cls, idEdificio, valor, periodo):
        deptos = DepartamentoService.filter_by(idEdificio=idEdificio)
        fecha = datetime.strptime(periodo, '%m-%Y')
        gastos = []
        for depto in deptos:
            if depto.estado != 'Habitado':
                continue
            gasto = cls.create(valor=valor, tipo='comun', descripcion='Gasto común', estado='pendiente', fecha=fecha.strftime("%d-%m-%Y"), idDepartamento=depto.idDepartamento)
            gastos.append(gasto)
        return gastos

class ServicioService(BaseService):
    
    _model = Servicio

class PersonaService(BaseService):

    _model = Persona

class ResidenteService(BaseService):

    _model = Residente

    @classmethod
    def filter_by_inicio(cls, year:int, mm:int=None, dd:int=None):
        query = cls._model.query.filter(
            extract('year', cls._model.inicio) == year
        )
        if mm is not None:
            query = query.filter(extract('month', cls._model.inicio) == mm)
        if dd is not None:
            query = query.filter(extract('day', cls._model.inicio) == dd)
        residentes = query.all()
        return residentes
    
    @classmethod
    def filter_by_termino(cls, year:int, mm:int=None, dd:int=None):
        query = cls._model.query.filter(
            extract('year', cls._model.termino) == year
        )
        if mm is not None:
            query = query.filter(extract('month', cls._model.termino) == mm)
        if dd is not None:
            query = query.filter(extract('day', cls._model.termino) == dd)
        residentes = query.all()
        return residentes
    
class PropietarioService(BaseService):

    _model = Propietario

    @classmethod
    def filter_by_inicio(cls, year:int, mm:int=None, dd:int=None):
        query = cls._model.query.filter(
            extract('year', cls._model.inicio) == year
        )
        if mm is not None:
            query = query.filter(extract('month', cls._model.inicio) == mm)
        if dd is not None:
            query = query.filter(extract('day', cls._model.inicio) == dd)
        propietarios = query.all()
        return propietarios
    
    @classmethod
    def filter_by_termino(cls, year:int, mm:int=None, dd:int=None):
        query = cls._model.query.filter(
            extract('year', cls._model.termino) == year
        )
        if mm is not None:
            query = query.filter(extract('month', cls._model.termino) == mm)
        if dd is not None:
            query = query.filter(extract('day', cls._model.termino) == dd)
        propietarios = query.all()
        return propietarios

class EmpleadoService(BaseService):

    _model = Empleado

class EmpleadoEdificioService(BaseService):

    _model = EmpleadoEdificio

    @classmethod
    def filter_by_inicio(cls, year:int, mm:int=None, dd:int=None):
        query = cls._model.query.filter(
            extract('year', cls._model.inicio) == year
        )
        if mm is not None:
            query = query.filter(extract('month', cls._model.inicio) == mm)
        if dd is not None:
            query = query.filter(extract('day', cls._model.inicio) == dd)
        empleados = query.all()
        return empleados
    
    @classmethod
    def filter_by_termino(cls, year:int, mm:int=None, dd:int=None):
        query = cls._model.query.filter(
            extract('year', cls._model.termino) == year
        )
        if mm is not None:
            query = query.filter(extract('month', cls._model.termino) == mm)
        if dd is not None:
            query = query.filter(extract('day', cls._model.termino) == dd)
        empleados = query.all()
        return empleados