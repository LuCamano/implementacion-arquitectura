from services import *

class BaseController:
    
    model: BaseService = None
    
    @classmethod
    def create(cls, **campos):
        return cls.model.create(**campos)
    
    @classmethod
    def get_all(cls):
        return cls.model.get_all()
    
    @classmethod
    def get_by_pk(cls, pk):
        return cls.model.get_by_pk(pk)
    
    @classmethod
    def update(cls, pk, **campos):
        return cls.model.update(pk, **campos)
    
    @classmethod
    def delete(cls, pk):
        return cls.model.delete(pk)
    
    @classmethod
    def filter_by(cls, **kwargs):
        return cls.model.filter_by(**kwargs)
    

class EdificioController(BaseController):
    
    model = EdificioService
    
class DepartamentoController(BaseController):
    
    model = DepartamentoService
    
class PagoController(BaseController):
    
    model = PagoService
    
    @classmethod
    def get_by_gasto(cls, idGasto):
        return cls.model.filter_by(idGasto=idGasto)
    
class GastoController(BaseController):
    
    model = GastoService
    
    @classmethod
    def hacerPago(cls, idGasto, monto):
        return GastoService(cls.model).hacer_pago(idGasto=idGasto, monto=monto)
    
    @classmethod
    def get_by_departamento(cls, idDepartamento):
        return GastoService(cls.model).get_by_departamento(idDepartamento)
    
class ServicioController(BaseController):
    
    model = ServicioService
    