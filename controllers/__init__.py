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
        return cls.filter_by(idGasto=idGasto)
    
class GastoController(BaseController):
    
    model = GastoService
    
    @classmethod
    def hacerPago(cls, idGasto, monto):
        return cls.model.hacer_pago(idGasto=idGasto, monto=monto)
    
    @classmethod
    def filter_by_date(cls, year:int, mm:int=None, dd:int=None):
        return cls.model.filter_by_date(year=year, mm=mm, dd=dd)

    @classmethod
    def get_by_departamento(cls, idDepartamento, estado=None):
        return cls.model.get_by_departamento(idDepartamento, estado)
    
    @classmethod
    def generar_gastos_comunes(cls, idEdificio, periodo, valor):
        return cls.model.generar_gastos_comunes(idEdificio=idEdificio, periodo=periodo, valor=valor)
    
class ServicioController(BaseController):
    
    model = ServicioService
    