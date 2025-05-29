# Imagen base
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia solo los requirements para instalar dependencias primero (mejor para caché)
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el proyecto
COPY . .

# Expone el puerto (Coolify lo usará)
EXPOSE 8001

# Comando de arranque con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001", ]