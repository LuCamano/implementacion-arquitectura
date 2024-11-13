from flask import Blueprint, request, jsonify
from controllers import *

edificio_blueprint = Blueprint('edificio', __name__)
departamento_blueprint = Blueprint('departamento', __name__)
pago_blueprint = Blueprint('pago', __name__)
gasto_blueprint = Blueprint('gasto', __name__)
servicio_blueprint = Blueprint('servicio', __name__)

class EdificioView:
    
    @staticmethod
    @edificio_blueprint.route('/edificio/create', methods=['POST'])
    def create():
        data = request.get_json()
        edificio = EdificioController.create(**data)
        return jsonify(edificio.serialize())
    
    @staticmethod
    @edificio_blueprint.route('/edificio/get_all', methods=['GET'])
    def get_all():
        edificios = EdificioController.get_all()
        return jsonify([edificio.serialize() for edificio in edificios])
    
    @staticmethod
    @edificio_blueprint.route('/edificio/get_by_pk/<int:idEdificio>', methods=['GET'])
    def get_by_pk(idEdificio):
        edificio = EdificioController.get_by_pk(idEdificio)
        return jsonify(edificio.serialize())
    
    @staticmethod
    @edificio_blueprint.route('/edificio/update/<int:idEdificio>', methods=['PUT'])
    def update(idEdificio):
        data = request.get_json()
        edificio = EdificioController.update(idEdificio, **data)
        return jsonify(edificio.serialize())
    
class DepartamentoView:
    
    @staticmethod
    @departamento_blueprint.route('/departamento/create', methods=['POST'])
    def create():
        data = request.get_json()
        departamento = DepartamentoController.create(**data)
        return jsonify(departamento.serialize())
    
    @staticmethod
    @departamento_blueprint.route('/departamento/get_all', methods=['GET'])
    def get_all():
        departamentos = DepartamentoController.get_all()
        return jsonify([departamento.serialize() for departamento in departamentos])
    
    @staticmethod
    @departamento_blueprint.route('/departamento/get_by_pk/<int:numero>/<int:idEdificio>', methods=['GET'])
    def get_by_pk(numero, idEdificio):
        departamento = DepartamentoController.get_by_pk(numero, idEdificio)
        return jsonify(departamento.serialize())
    
    @staticmethod
    @departamento_blueprint.route('/departamento/update/<int:numero>/<int:idEdificio>', methods=['PUT'])
    def update(numero, idEdificio):
        data = request.get_json()
        departamento = DepartamentoController.update(numero, idEdificio, **data)
        return jsonify(departamento.serialize())
    
class PagoView:
    
    @staticmethod
    @pago_blueprint.route('/pago/create', methods=['POST'])
    def create():
        data = request.get_json()
        pago = PagoController.create(**data)
        return jsonify(pago.serialize())
    
    @staticmethod
    @pago_blueprint.route('/pago/get_all', methods=['GET'])
    def get_all():
        pagos = PagoController.get_all()
        return jsonify([pago.serialize() for pago in pagos])
    
    @staticmethod
    @pago_blueprint.route('/pago/get_by_pk/<int:idPago>', methods=['GET'])
    def get_by_pk(idPago):
        pago = PagoController.get_by_pk(idPago)
        return jsonify(pago.serialize())
    
    @staticmethod
    @pago_blueprint.route('/pago/update/<int:idPago>', methods=['PUT'])
    def update(idPago):
        data = request.get_json()
        pago = PagoController.update(idPago, **data)
        return jsonify(pago.serialize())
    
class GastoView:
    
    @staticmethod
    @gasto_blueprint.route('/gasto/create', methods=['POST'])
    def create():
        data = request.get_json()
        gasto = GastoController.create(**data)
        return jsonify(gasto.serialize())
    
    @staticmethod
    @gasto_blueprint.route('/gasto/get_all', methods=['GET'])
    def get_all():
        gastos = GastoController.get_all()
        return jsonify([gasto.serialize() for gasto in gastos])
    
    @staticmethod
    @gasto_blueprint.route('/gasto/get_by_pk/<int:idGasto>', methods=['GET'])
    def get_by_pk(idGasto):
        gasto = GastoController.get_by_pk(idGasto)
        return jsonify(gasto.serialize())
    
    @staticmethod
    @gasto_blueprint.route('/gasto/update/<int:idGasto>', methods=['PUT'])
    def update(idGasto):
        data = request.get_json()
        gasto = GastoController.update(idGasto, **data)
        return jsonify(gasto.serialize())
    
class ServicioView:
    
    @staticmethod
    @servicio_blueprint.route('/servicio/create', methods=['POST'])
    def create():
        data = request.get_json()
        servicio = ServicioController.create(**data)
        return jsonify(servicio.serialize())
    
    @staticmethod
    @servicio_blueprint.route('/servicio/get_all', methods=['GET'])
    def get_all():
        servicios = ServicioController.get_all()
        return jsonify([servicio.serialize() for servicio in servicios])
    
    @staticmethod
    @servicio_blueprint.route('/servicio/get_by_pk/<int:idServicio>', methods=['GET'])
    def get_by_pk(idServicio):
        servicio = ServicioController.get_by_pk(idServicio)
        return jsonify(servicio.serialize())
    
    @staticmethod
    @servicio_blueprint.route('/servicio/update/<int:idServicio>', methods=['PUT'])
    def update(idServicio):
        data = request.get_json()
        servicio = ServicioController.update(idServicio, **data)
        return jsonify(servicio.serialize())