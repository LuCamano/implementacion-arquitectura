from app import create_app
from views import edificio_blueprint, departamento_blueprint, pago_blueprint, gasto_blueprint, servicio_blueprint, empleado_edificio_blueprint, empleado_blueprint, persona_blueprint, residente_blueprint, propietario_blueprint

app = create_app()
app.register_blueprint(edificio_blueprint)
app.register_blueprint(departamento_blueprint)
app.register_blueprint(pago_blueprint)
app.register_blueprint(gasto_blueprint)
app.register_blueprint(servicio_blueprint)
app.register_blueprint(empleado_edificio_blueprint)
app.register_blueprint(empleado_blueprint)
app.register_blueprint(persona_blueprint)
app.register_blueprint(residente_blueprint)
app.register_blueprint(propietario_blueprint)

if __name__ == '__main__':
    app.run()