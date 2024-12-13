from flask import Blueprint, request, jsonify
from controllers import *

edificio_blueprint = Blueprint('edificio', __name__)
departamento_blueprint = Blueprint('departamento', __name__)
pago_blueprint = Blueprint('pago', __name__)
gasto_blueprint = Blueprint('gasto', __name__)
servicio_blueprint = Blueprint('servicio', __name__)
persona_blueprint = Blueprint('persona', __name__)
residente_blueprint = Blueprint('residente', __name__)
propietario_blueprint = Blueprint('propietario', __name__)
empleado_blueprint = Blueprint('empleado', __name__)
empleado_edificio_blueprint = Blueprint('empleado_edificio', __name__)

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
                if c == 'valor':
                    filtro[c] = int(valor)
                else: 
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
        parametros = ['year','mm','dd']
        # Crear un filtro vacío
        campos = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                campos[c] = valor
        try:
            if len(campos) > 0:
                if 'year' in campos:
                    for key, val in campos.items():
                        campos[key] = int(val)
                    gastos = GastoController.filter_by_date(**campos)
                    return jsonify([gasto.serialize() for gasto in gastos])
                else:
                    raise Exception("debe ingresar al menos un año para la consulta")
            else:
                raise Exception("debe ingresar al menos un año para la consulta")
        except Exception as e:
            return jsonify({'error': str(e)})

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
    
class PersonaView:

    @staticmethod
    @persona_blueprint.route('/persona/create', methods=['POST'])
    def create():
        try:
            data = request.get_json()
            persona = PersonaController.create(**data)
            return jsonify(persona.serialize())
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @staticmethod
    @persona_blueprint.route('/persona/all', methods=['GET'])
    def get_all():
        # Obtener los parámetros de consulta
        parametros = ['nombre', 'apellido', 'contacto', 'conEmergencia']
        # Crear un filtro vacío
        filtro = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                filtro[c] = valor
        # Obtener los departamentos
        if len(filtro) > 0:
            personas = PersonaController.filter_by(**filtro)
        else:
            personas = PersonaController.get_all()
        return jsonify([persona.serialize() for persona in personas])
    
    @staticmethod
    @persona_blueprint.route('/persona/<string:run>', methods=['GET'])
    def get_by_pk(run):
        persona = PersonaController.get_by_pk(run)
        return jsonify(persona.serialize())
    
    @staticmethod
    @persona_blueprint.route('/persona/update/<string:run>', methods=['PUT'])
    def update(run):
        try:
            data = request.get_json()
            persona = PersonaController.update(run, **data)
            return jsonify(persona.serialize())
        except Exception as e:
            return jsonify({'error': str(e)})
    
class ResidenteView:
    
    @staticmethod
    @residente_blueprint.route('/residente/create', methods=['POST'])
    def create():
        try:
            data = request.get_json()
            residente = ResidenteController.create(**data)
            return jsonify(residente.serialize())
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @staticmethod
    @residente_blueprint.route('/residente/all', methods=['GET'])
    def get_all():
        # Obtener los parámetros de consulta
        parametros = ['run', 'idDepartamento']
        # Crear un filtro vacío
        filtro = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                filtro[c] = valor
        # Obtener los departamentos
        if len(filtro) > 0:
            residentes = ResidenteController.filter_by(**filtro)
        else:
            residentes = ResidenteController.get_all()
        return jsonify([residente.serialize() for residente in residentes])
    
    @staticmethod
    @residente_blueprint.route('/residente/<int:idResidente>', methods=['GET'])
    def get_by_pk(idResidente):
        residente = ResidenteController.get_by_pk(idResidente)
        return jsonify(residente.serialize())
    
    @staticmethod
    @residente_blueprint.route('/residente/update/<int:idResidente>', methods=['PUT'])
    def update(idResidente):
        try:
            data = request.get_json()
            residente = ResidenteController.update(idResidente, **data)
            return jsonify(residente.serialize())
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @staticmethod
    @residente_blueprint.route('/residente/inicio', methods=['GET'])
    def filter_by_inicio():
        # Obtener los parámetros de consulta
        parametros = ['year','mm','dd']
        # Crear un filtro vacío
        campos = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                campos[c] = valor
        try:
            if len(campos) > 0:
                if 'year' in campos:
                    for key, val in campos.items():
                        campos[key] = int(val)
                    residentes = ResidenteController.filter_by_date(**campos)
                    return jsonify([residente.serialize() for residente in residentes])
                else:
                    raise Exception("debe ingresar al menos un año para la consulta")
            else:
                raise Exception("debe ingresar al menos un año para la consulta")
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @staticmethod
    @residente_blueprint.route('/residente/termino', methods=['GET'])
    def filter_by_termino():
        # Obtener los parámetros de consulta
        parametros = ['year','mm','dd']
        # Crear un filtro vacío
        campos = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                campos[c] = valor
        try:
            if len(campos) > 0:
                if 'year' in campos:
                    for key, val in campos.items():
                        campos[key] = int(val)
                    residentes = ResidenteController.filter_by_date(**campos)
                    return jsonify([residente.serialize() for residente in residentes])
                else:
                    raise Exception("debe ingresar al menos un año para la consulta")
            else:
                raise Exception("debe ingresar al menos un año para la consulta")
        except Exception as e:
            return jsonify({'error': str(e)})

class PropietarioView:

    @staticmethod
    @propietario_blueprint.route('/propietario/create', methods=['POST'])
    def create():
        try:
            data = request.get_json()
            propietario = PropietarioController.create(**data)
            return jsonify(propietario.serialize())
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @staticmethod
    @propietario_blueprint.route('/propietario/all', methods=['GET'])
    def get_all():
        # Obtener los parámetros de consulta
        parametros = ['run', 'idDepartamento']
        # Crear un filtro vacío
        filtro = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                filtro[c] = valor
        # Obtener los departamentos
        if len(filtro) > 0:
            propietarios = PropietarioController.filter_by(**filtro)
        else:
            propietarios = PropietarioController.get_all()
        return jsonify([propietario.serialize() for propietario in propietarios])
    
class EmpleadoView:

    @staticmethod
    @empleado_blueprint.route('/empleado/create', methods=['POST'])
    def create():
        try:
            data = request.get_json()
            empleado = EmpleadoController.create(**data)
            return jsonify(empleado.serialize())
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @staticmethod
    @empleado_blueprint.route('/empleado/all', methods=['GET'])
    def get_all():
        # Obtener los parámetros de consulta
        parametros = ['nombre', 'sueldoHora', 'horas', 'contacto', 'conEmergencia', 'tipo']
        # Crear un filtro vacío
        filtro = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                filtro[c] = valor
        # Obtener los departamentos
        if len(filtro) > 0:
            empleados = EmpleadoController.filter_by(**filtro)
        else:
            empleados = EmpleadoController.get_all()
        return jsonify([empleado.serialize() for empleado in empleados])
    
    @staticmethod
    @empleado_blueprint.route('/empleado/<string:run>', methods=['GET'])
    def get_by_pk(run):
        empleado = EmpleadoController.get_by_pk(run)
        return jsonify(empleado.serialize())
    
    @staticmethod
    @empleado_blueprint.route('/empleado/update/<string:run>', methods=['PUT'])
    def update(run):
        try:
            data = request.get_json()
            empleado = EmpleadoController.update(run, **data)
            return jsonify(empleado.serialize())
        except Exception as e:
            return jsonify({'error': str(e)})
    
class EmpleadoEdificioView:

    @staticmethod
    @empleado_edificio_blueprint.route('/empleado-edificio/create', methods=['POST'])
    def create():
        try:
            data = request.get_json()
            empleado_edificio = EmpleadoEdificioController.create(**data)
            return jsonify(empleado_edificio.serialize())
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @staticmethod
    @empleado_edificio_blueprint.route('/empleado-edificio/all', methods=['GET'])
    def get_all():
        # Obtener los parámetros de consulta
        parametros = ['run', 'idEdificio']
        # Crear un filtro vacío
        filtro = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                filtro[c] = valor
        # Obtener los departamentos
        if len(filtro) > 0:
            empleados_edificio = EmpleadoEdificioController.filter_by(**filtro)
        else:
            empleados_edificio = EmpleadoEdificioController.get_all()
        return jsonify([empleado_edificio.serialize() for empleado_edificio in empleados_edificio])
    
    @staticmethod
    @empleado_edificio_blueprint.route('/empleado-edificio/<int:idEmpleadoEdificio>', methods=['GET'])
    def get_by_pk(idEmpleadoEdificio):
        try:
            empleado_edificio = EmpleadoEdificioController.get_by_pk(idEmpleadoEdificio)
            return jsonify(empleado_edificio.serialize())
        except Exception as e:
            return jsonify({'error': str(e)})
        
    @staticmethod
    @empleado_edificio_blueprint.route('/empleado-edificio/update/<int:idEmpleadoEdificio>', methods=['PUT'])
    def update(idEmpleadoEdificio):
        try:
            data = request.get_json()
            empleado_edificio = EmpleadoEdificioController.update(idEmpleadoEdificio, **data)
            return jsonify(empleado_edificio.serialize())
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @staticmethod
    @empleado_edificio_blueprint.route('/empleado-edificio/termino', methods=['GET'])
    def filter_by_termino():
        # Obtener los parámetros de consulta
        parametros = ['year','mm','dd']
        # Crear un filtro vacío
        campos = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                campos[c] = valor
        try:
            if len(campos) > 0:
                if 'year' in campos:
                    for key, val in campos.items():
                        campos[key] = int(val)
                    empleados_edificio = EmpleadoEdificioController.filter_by_termino(**campos)
                    return jsonify([empleado_edificio.serialize() for empleado_edificio in empleados_edificio])
                else:
                    raise Exception("debe ingresar al menos un año para la consulta")
            else:
                raise Exception("debe ingresar al menos un año para la consulta")
        except Exception as e:
            return jsonify({'error': str(e)})
    
    @staticmethod
    @empleado_edificio_blueprint.route('/empleado-edificio/inicio', methods=['GET'])
    def filter_by_inicio():
        # Obtener los parámetros de consulta
        parametros = ['year','mm','dd']
        # Crear un filtro vacío
        campos = {}
        # Recorrer los parámetros de consulta
        for c in parametros:
            valor = request.args.get(c)
            if valor is not None:
                campos[c] = valor
        try:
            if len(campos) > 0:
                if 'year' in campos:
                    for key, val in campos.items():
                        campos[key] = int(val)
                    empleados_edificio = EmpleadoEdificioController.filter_by_inicio(**campos)
                    return jsonify([empleado_edificio.serialize() for empleado_edificio in empleados_edificio])
                else:
                    raise Exception("debe ingresar al menos un año para la consulta")
            else:
                raise Exception("debe ingresar al menos un año para la consulta")
        except Exception as e:
            return jsonify({'error': str(e)})
