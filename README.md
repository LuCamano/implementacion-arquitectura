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
    - **Ruta:** `/edificio/all`
    - **Método:** `GET`
    - **Parámetros opcionales:**
        - `nombre`: Filtrar por nombre del edificio
        - `direccion`: Filtrar por dirección del edificio
        - `numPisos`: Filtrar por número de pisos del edificio
    - **Ejemplo:**
        ```sh
        curl -X GET "http://127.0.0.1:5000/edificio/all?nombre=Edificio1"
        ```

- **Obtener Edificio por ID**
    - **Ruta:** `/edificio/<int:idEdificio>`
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
            "estado": "Desocupado",
            "idEdificio": 1
        }
        ```

- **Obtener Todos los Departamentos**
    - **Ruta:** `/departamento/all`
    - **Método:** `GET`
    - **Parámetros opcionales:**
        - `numero`: Filtrar por número del departamento
        - `piso`: Filtrar por piso del departamento
        - `estado`: Filtrar por estado del departamento
        - `idEdificio`: Filtrar por ID del edificio
    - **Ejemplo:**
        ```sh
        curl -X GET "http://127.0.0.1:5000/departamento/all?estado=Desocupado"
        ```

- **Obtener Departamento por PK**
    - **Ruta:** `/departamento/<int:idDepartamento>`
    - **Método:** `GET`

- **Actualizar Departamento**
    - **Ruta:** `/departamento/update/<int:idDepartamento>`
    - **Método:** `PUT`
    - **Datos:**
        ```json
        {
            "estado": "Habitado"
        }
        ```

### Pago

- **Obtener Todos los Pagos**
    - **Ruta:** `/pago/all`
    - **Método:** `GET`

- **Obtener Pago por PK**
    - **Ruta:** `/pago/<int:idPago>`
    - **Método:** `GET`

- **Obtener Pagos por Gasto**
    - **Ruta:** `/pago/by_gasto/<int:idGasto>`
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
    - **Ruta:** `/gasto/all`
    - **Método:** `GET`
    - **Parámetros opcionales:**
        - `valor`: Filtrar por valor del gasto
        - `tipo`: Filtrar por tipo de gasto
        - `descripcion`: Filtrar por descripción del gasto
        - `estado`: Filtrar por estado del gasto
    - **Ejemplo:**
        ```sh
        curl -X GET "http://127.0.0.1:5000/gasto/all?estado=pendiente"
        ```

- **Filtrar Gastos por Fecha**
    - **Ruta:** `/gasto/periodo`
    - **Método:** `GET`
    - **Parámetros opcionales:**
        - `year` (obligatorio): Año del gasto
        - `mm`: Mes del gasto
        - `dd`: Día del gasto
    - **Ejemplo:**
        ```sh
        curl -X GET "http://127.0.0.1:5000/gasto/periodo?year=2023&mm=10"
        ```

- **Obtener Gasto por PK**
    - **Ruta:** `/gasto/<int:idGasto>`
    - **Método:** `GET`

- **Actualizar Gasto**
    - **Ruta:** `/gasto/update/<int:idGasto>`
    - **Método:** `PUT`
    - **Datos:**
        ```json
        {
            "estado": "pagado"
        }
        ```

- **Hacer Pago de Gasto**
    - **Ruta:** `/gasto/hacer_pago/<int:idGasto>/<int:monto>`
    - **Método:** `POST`

- **Obtener Gastos por Departamento**
    - **Ruta:** `/gasto/by_departamento/<int:idDepartamento>`
    - **Método:** `GET`

- **Generar Gastos Comunes**
    - **Ruta:** `/gasto/generar_gastos_comunes`
    - **Método:** `POST`
    - **Datos:**
        ```json
        {
            "idEdificio": 1,
            "valor": 5000,
            "periodo": "10-2023"
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
    - **Ruta:** `/servicio/all`
    - **Método:** `GET`

- **Obtener Servicio por PK**
    - **Ruta:** `/servicio/<int:idServicio>`
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
