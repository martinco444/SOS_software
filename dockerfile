FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

# Recopilar archivos estáticos
RUN python manage.py collectstatic --noinput

# El comando se configurará en Railway
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]