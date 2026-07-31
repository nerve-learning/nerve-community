from fastapi import FastAPI, Response, status
from nerve import NexusClient
from fastapi.middleware.cors import CORSMiddleware

client = NexusClient()

app = FastAPI(
    title="Reto 08 — Puente HTTP para Nerve (FastAPI) #8",
    description="API Solución reto #8",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", summary="Probar conexion a la API.")
def test(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"status": 200, "details": "API funcionando correctamente"}


@app.post("/login", summary="Conectarse a NERVE.")
def login(name_user: str, response: Response):
    try:
        if not name_user or not name_user.strip():
            raise ValueError("El name_user no puede estar vacío.")

        if not isinstance(name_user, str) or not isinstance(name_user, str):
            raise TypeError("El name_user debe ser texto (str).")

        client.connect(name_user)
        response.status_code = status.HTTP_200_OK
        return {"status": 200, "details": f"Conectado con el user: {name_user}"}

    except (ValueError, TypeError) as ev:
        response.status_code = status.HTTP_422_UNPROCESSABLE_CONTENT
        return {"status": 422, "details": f"Error de Validación: {ev}"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": 500, "details": str(e)}


@app.post("/enviar", summary="Enviar mensaje a otro usuario via NERVE.")
def enviar_nerve(destino: str, mensaje: str, response: Response):
    try:
        if not destino or not destino.strip():
            raise ValueError("El destino no puede estar vacío.")
        if not mensaje or not mensaje.strip():
            raise ValueError("El mensaje no puede estar vacío.")

        if not isinstance(destino, str) or not isinstance(mensaje, str):
            raise TypeError("Ambos campos deben ser texto (str).")

        msg_json = {"to": destino, "msg": mensaje}

        client.send(destino, msg_json)
        response.status_code = status.HTTP_200_OK
        return {"status": 200, "details": {"to": destino, "payload": msg_json}}
    except (ValueError, TypeError) as ev:
        response.status_code = status.HTTP_422_UNPROCESSABLE_CONTENT
        return {"status": 422, "details": f"Error de Validación: {ev}"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": 500, "details": str(e)}


@app.post("/enviar-all", summary="Enviar mensaje a TODOS los clientes via NERVE.")
def enviar_nerve_all(mensaje: str, response: Response):
    try:
        if not mensaje or not mensaje.strip():
            raise ValueError("El mensaje no puede estar vacío.")

        if not isinstance(mensaje, str):
            raise TypeError("MENSAJE debe ser texto (str).")

        msg_json = {"msg": mensaje}

        client.broadcast(msg_json)
        response.status_code = status.HTTP_200_OK
        return {"status": 200, "details": {"to": "all", "payload": msg_json}}
    except (ValueError, TypeError) as ev:
        response.status_code = status.HTTP_422_UNPROCESSABLE_CONTENT
        return {"status": 422, "details": f"Error de Validación: {ev}"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": 500, "details": str(e)}


@app.delete("/logout", summary="Desconectarse de NERVE.")
def disconnect(response: Response):
    try:
        client.disconnect()
        response.status_code = status.HTTP_200_OK
        return {"status": 200, "details": "Desconexión exitosa."}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status": 500, "details": str(e)}
