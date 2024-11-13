from services import *

class EdificioController:
    @staticmethod
    def create(**campos):
        return EdificioService.create(**campos)
    
    @staticmethod
    def get_all():
        return EdificioService.get_all()
    
    @staticmethod
    def get_by_pk(idEdificio):
        return EdificioService.get_by_pk(idEdificio)
    
    @staticmethod
    def update(idEdificio, **campos):
        return EdificioService.update(idEdificio, **campos)
    
class DepartamentoController:
    @staticmethod
    def create(**campos):
        return DepartamentoService.create(**campos)
    
    @staticmethod
    def get_all():
        return DepartamentoService.get_all()
    
    @staticmethod
    def get_by_pk(numero, idEdificio):
        return DepartamentoService.get_by_pk(numero, idEdificio)
    
    @staticmethod
    def update(numero, idEdificio, **campos):
        return DepartamentoService.update(numero, idEdificio, **campos)
    
class PagoController:
    @staticmethod
    def create(**campos):
        return PagoService.create(**campos)
    
    @staticmethod
    def get_all():
        return PagoService.get_all()
    
    @staticmethod
    def get_by_pk(idPago):
        return PagoService.get_by_pk(idPago)
    
    @staticmethod
    def update(idGasto, numero, idEdificio, **campos):
        return PagoService.update(idGasto, numero, idEdificio, **campos)
    
class GastoController:
    @staticmethod
    def create(**campos):
        return GastoService.create(**campos)
    
    @staticmethod
    def get_all():
        return GastoService.get_all()
    
    @staticmethod
    def get_by_pk(idGasto):
        return GastoService.get_by_pk(idGasto)
    
    @staticmethod
    def update(idGasto, **campos):
        return GastoService.update(idGasto, **campos)
    
class ServicioController:
    @staticmethod
    def create(**campos):
        return ServicioService.create(**campos)
    
    @staticmethod
    def get_all():
        return ServicioService.get_all()
    
    @staticmethod
    def get_by_pk(idServicio):
        return ServicioService.get_by_pk(idServicio)
    
    @staticmethod
    def update(nombre, **campos):
        return ServicioService.update(nombre, **campos)