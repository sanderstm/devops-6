import os
from asgiref.wsgi import WsgiToAsgi
from app import create_app

# Crear la app Flask
flask_app = create_app()

# Convertir Flask a una aplicación ASGI
asgi_app = WsgiToAsgi(flask_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(asgi_app, host="0.0.0.0", port=5000)
