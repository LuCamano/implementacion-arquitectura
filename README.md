# Implementación de Pago de Gastos Comunes

Este proyecto es una API para la gestión de pagos de gastos comunes en un edificio. La API permite crear, obtener y actualizar información sobre edificios, departamentos, pagos, gastos y servicios.

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/LuCamano/implementacion-arquitectura
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd implementacion-arquitectura
    ```
3. Crea un entorno virtual:
    ```sh
    python -m venv venv
    ```
4. Activa el entorno virtual:
    - En Windows:
        ```sh
        venv\Scripts\activate
        ```
    - En macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Inicia la aplicación:
    ```sh
    python run.py
    ```
2. La API estará disponible en `http://127.0.0.1:5000`.

## Rutas

### Edificio

- **Crear Edificio**
    - **Ruta:** `/edificio/create`
    - **Método:** `POST`
    - **Datos:**
        ```json
        {
            "nombre": "Edificio A",
            "direccion": "Calle Falsa 123",
            "numPisos": 10
        }
        ```

- **Obtener Todos los Edificios**
    - **Ruta:** `/edificio/get_all`
    - **Método:** `GET`

- **Obtener Edificio por ID**
    - **Ruta:** `/edificio/get_by_pk/<int:idEdificio>`
    - **Método:** `GET`

- **Actualizar Edificio**
    - **Ruta:** `/edificio/update/<int:idEdificio>`
    - **Método:** `PUT`
    - **Datos:**
        ```json
        {
            "nombre": "Edificio B",
            "direccion": "Calle Verdadera 456",
            "numPisos": 12
        }
        ```

### Departamento

- **Crear Departamento**
    - **Ruta:** `/departamento/create`
    - **Método:** `POST`
    - **Datos:**
        ```json
        {
            "numero": 101,
            "piso": 1,
            "estado": "Disponible",
            "idEdificio": 1
        }
        ```

- **Obtener Todos los Departamentos**
    - **Ruta:** `/departamento/get_all`
    - **Método:** `GET`

- **Obtener Departamento por PK**
    - **Ruta:** `/departamento/get_by_pk/<int:numero>/<int:idEdificio>`
    - **Método:** `GET`

- **Actualizar Departamento**
    - **Ruta:** `/departamento/update/<int:numero>/<int:idEdificio>`
    - **Método:** `PUT`
    - **Datos:**
        ```json
        {
            "estado": "Ocupado"
        }
        ```

### Pago

- **Obtener Todos los Pagos**
    - **Ruta:** `/pago/get_all`
    - **Método:** `GET`

- **Obtener Pago por PK**
    - **Ruta:** `/pago/get_by_pk/<int:idPago>`
    - **Método:** `GET`

- **Obtener Pagos por Gasto**
    - **Ruta:** `/pago/get_by_gasto/<int:idGasto>`
    - **Método:** `GET`

- **Obtener Pagos por Departamento**
    - **Ruta:** `/pago/get_by_departamento/<int:numero>/<int:idEdificio>`
    - **Método:** `GET`

### Gasto

- **Crear Gasto**
    - **Ruta:** `/gasto/create`
    - **Método:** `POST`
    - **Datos:**
        ```json
        {
            "valor": 10000,
            "tipo": "Mantenimiento",
            "descripcion": "Reparación de ascensor",
            "estado": "Pendiente",
            "fecha": "01-10-2023"
        }
        ```

- **Obtener Todos los Gastos**
    - **Ruta:** `/gasto/get_all`
    - **Método:** `GET`

- **Obtener Gasto por PK**
    - **Ruta:** `/gasto/get_by_pk/<int:idGasto>`
    - **Método:** `GET`

- **Actualizar Gasto**
    - **Ruta:** `/gasto/update/<int:idGasto>`
    - **Método:** `PUT`
    - **Datos:**
        ```json
        {
            "estado": "Pagado"
        }
        ```

- **Hacer Pago de Gasto**
    - **Ruta:** `/gasto/hacer_pago/<int:idGasto>`
    - **Método:** `POST`
    - **Datos:**
        ```json
        {
            "numero": 101,
            "idEdificio": 1,
            "monto": 5000
        }
        ```

### Servicio

- **Crear Servicio**
    - **Ruta:** `/servicio/create`
    - **Método:** `POST`
    - **Datos:**
        ```json
        {
            "nombre": "Limpieza",
            "descripcion": "Limpieza de áreas comunes",
            "idGasto": 1
        }
        ```

- **Obtener Todos los Servicios**
    - **Ruta:** `/servicio/get_all`
    - **Método:** `GET`

- **Obtener Servicio por PK**
    - **Ruta:** `/servicio/get_by_pk/<int:idServicio>`
    - **Método:** `GET`

- **Actualizar Servicio**
    - **Ruta:** `/servicio/update/<int:idServicio>`
    - **Método:** `PUT`
    - **Datos:**
        ```json
        {
            "descripcion": "Limpieza de áreas comunes y jardines"
        }
        ```
