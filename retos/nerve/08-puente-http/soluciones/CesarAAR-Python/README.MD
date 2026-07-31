# Solución Reto Nerve #08 Puente HTTP

## Estructura
```text
CesarAAR-Python
├── main.py #Programa principal. Aquí está toda la logica.
├── requirements.txt #Requerimientos de instalación.
└── test.py #Programa secundario. Pograma para ejecutar para comprobar el funcionamiento de la api.
```

## Pasos de uso 
1.  Crear entorno virtual e instalar dependencias:

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```
2. Ejecutar NERVE:
```bash
nerve start
```

3. Ejecutar la API:

```bash
uvicorn main:app --reload
```
e ingresar a la documentación: `http://127.0.0.1:8000/docs`.

4. Ejecutar el oyente:
```bash
python test.py
```
## Opciones de la API
- */*: Verifica el estado de la API
- */login*: Crea el cliente(usuario) en NERVE
- */enviar*: Envias un mensaje a un cliente destino (el de test.py = test2).
- */enviar-all*: Envias el mensaje a todos los clientes.
- */logout*: Desconectas al cliente.