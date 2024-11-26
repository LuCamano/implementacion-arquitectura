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
    @edificio_blueprint.route('/edificio/all', methods=['GET'])
    def get_all():
        # Obtener los parámetros de consulta
        parametros = ['nombre', 'direccion', 'numPisos']
        # Crear un filtro vacío
        filtro = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                filtro[c] = valor
        # Obtener los edificios
        if len(filtro) > 0:
            edificios = EdificioController.filter_by(**filtro)
        else:
            edificios = EdificioController.get_all()
        return jsonify([edificio.serialize() for edificio in edificios])
    
    @staticmethod
    @edificio_blueprint.route('/edificio/<int:idEdificio>', methods=['GET'])
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
    @departamento_blueprint.route('/departamento/all', methods=['GET'])
    def get_all():
        # Obtener los parámetros de consulta
        parametros = ['numero', 'piso', 'estado', 'idEdificio']
        # Crear un filtro vacío
        filtro = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                filtro[c] = valor
        # Obtener los departamentos
        if len(filtro) > 0:
            departamentos = DepartamentoController.filter_by(**filtro)
        else:
            departamentos = DepartamentoController.get_all()
        return jsonify([departamento.serialize() for departamento in departamentos])
    
    @staticmethod
    @departamento_blueprint.route('/departamento/<int:idDepartamento>', methods=['GET'])
    def get_by_pk(idDepartamento):
        departamento = DepartamentoController.get_by_pk(idDepartamento)
        return jsonify(departamento.serialize())
    
    @staticmethod
    @departamento_blueprint.route('/departamento/update/<int:idDepartamento>', methods=['PUT'])
    def update(idDepartamento):
        data = request.get_json()
        departamento = DepartamentoController.update(idDepartamento, **data)
        return jsonify(departamento.serialize())
    
class PagoView:

    @staticmethod
    @pago_blueprint.route('/pago/all', methods=['GET'])
    def get_all():
        pagos = PagoController.get_all()
        return jsonify([pago.serialize() for pago in pagos])
    
    @staticmethod
    @pago_blueprint.route('/pago/<int:idPago>', methods=['GET'])
    def get_by_pk(idPago):
        pago = PagoController.get_by_pk(idPago)
        return jsonify(pago.serialize())
    
    @staticmethod
    @pago_blueprint.route('/pago/by_gasto/<int:idGasto>', methods=['GET'])
    def get_by_gasto(idGasto):
        pagos = PagoController.get_by_gasto(idGasto)
        return jsonify({'pagos':[pago.serialize() for pago in pagos]})
    
class GastoView:
    
    @staticmethod
    @gasto_blueprint.route('/gasto/create', methods=['POST'])
    def create():
        data = request.get_json()
        gasto = GastoController.create(**data)
        return jsonify(gasto.serialize())
    
    @staticmethod
    @gasto_blueprint.route('/gasto/all', methods=['GET'])
    def get_all():
        # Obtener los parámetros de consulta
        parametros = ['valor', 'tipo', 'descripcion', 'estado']
        # Crear un filtro vacío
        filtro = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                filtro[c] = valor
        # Obtener los gastos
        if len(filtro) > 0:
            gastos = GastoController.filter_by(**filtro)
        else:
            gastos = GastoController.get_all()
        return jsonify([gasto.serialize() for gasto in gastos])
    
    @staticmethod
    @gasto_blueprint.route('/gasto/periodo', methods=['GET'])
    def filter_by_date():
        # Obtener los parámetros de consulta
        parametros = ['day','month','year']
        # Crear un filtro vacío
        campos = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                campos[c] = valor
        try:
            if len(campos) > 0:
                pass
            else:
                raise Exception("debe ingresar al menos un año para la consulta")
        except Exception as e:
            return jsonify(e)
            

    @staticmethod
    @gasto_blueprint.route('/gasto/<int:idGasto>', methods=['GET'])
    def get_by_pk(idGasto):
        gasto = GastoController.get_by_pk(idGasto)
        return jsonify(gasto.serialize())
    
    @staticmethod
    @gasto_blueprint.route('/gasto/update/<int:idGasto>', methods=['PUT'])
    def update(idGasto):
        data = request.get_json()
        gasto = GastoController.update(idGasto, **data)
        return jsonify(gasto.serialize())
    
    @staticmethod
    @gasto_blueprint.route('/gasto/hacer_pago/<int:idGasto>/<int:monto>', methods=['POST'])
    def hacerPago(idGasto, monto):
        try:
            gasto, pagos, por_pagar, total_pagado = GastoController.hacerPago(idGasto, monto)
            return jsonify({'total-pagado': total_pagado, 'por-pagar': por_pagar, 'gasto': gasto.serialize(), 'pagos': [pago.serialize() for pago in pagos]})
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @staticmethod
    @gasto_blueprint.route('/gasto/by_departamento/<int:idDepartamento>', methods=['GET'])
    def get_by_departamento(idDepartamento):
        estado = request.args.get('estado')
        gastos = GastoController.get_by_departamento(idDepartamento, estado)
        return jsonify([gasto.serialize() for gasto in gastos])
    
    @staticmethod
    @gasto_blueprint.route('/gasto/generar_gastos_comunes', methods=['POST'])
    def generarGastosComunes():
        try:
            data = request.get_json()
            gastos = GastoController.generar_gastos_comunes(**data)
            return jsonify([gasto.serialize() for gasto in gastos])
        except Exception as e:
            return jsonify({'error': str(e)})
class ServicioView:
    
    @staticmethod
    @servicio_blueprint.route('/servicio/create', methods=['POST'])
    def create():
        data = request.get_json()
        servicio = ServicioController.create(**data)
        return jsonify(servicio.serialize())
    
    @staticmethod
    @servicio_blueprint.route('/servicio/all', methods=['GET'])
    def get_all():
        servicios = ServicioController.get_all()
        return jsonify([servicio.serialize() for servicio in servicios])
    
    @staticmethod
    @servicio_blueprint.route('/servicio/<int:idServicio>', methods=['GET'])
    def get_by_pk(idServicio):
        servicio = ServicioController.get_by_pk(idServicio)
        return jsonify(servicio.serialize())
    
    @staticmethod
    @servicio_blueprint.route('/servicio/update/<int:idServicio>', methods=['PUT'])
    def update(idServicio):
        data = request.get_json()
        servicio = ServicioController.update(idServicio, **data)
        return jsonify(servicio.serialize())