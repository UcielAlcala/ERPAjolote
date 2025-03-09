# backend/Dockerfile

FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip

# Instalar dependencias del sistema
RUN apk update && apk add --no-cache \
    postgresql-dev \
    gcc \
    python3-dev \
    musl-dev \
    libpq

# Copia tu paquete `printer_farm_controller`
COPY ./bpf /app/bpf

# Copiar y instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/

# Recolectar estáticos (asumiendo que tu settings.py está configurado)
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:8000", "erp_backend.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]


