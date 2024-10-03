
FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE crm_oxi.settings


CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000