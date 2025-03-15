# Usa una imagen base ligera de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /flask-server

# Copia los archivos de la aplicación
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

# Comando para ejecutar la aplicación en producción con uvicorn
CMD ["uvicorn", "run:asgi_app", "--host", "0.0.0.0", "--port", "5000"]


