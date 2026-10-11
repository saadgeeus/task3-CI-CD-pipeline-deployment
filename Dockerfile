FROM python:3.8-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir gunicorn ruff

COPY . .

EXPOSE 8000

# Pehle migrations run hongi, phir Gunicorn server start hoga
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 todoApp.wsgi:application"]