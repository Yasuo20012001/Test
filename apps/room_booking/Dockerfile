FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 0
ENV PYTHONUNBUFFERED 0

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
EXPOSE 8001
COPY . .
CMD python manage.py runserver 0.0.0.0:8001