FROM python:3.10.2-alpine

RUN apk add gcc musl-dev mariadb-connector-c-dev

WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt

EXPOSE 8000
CMD python manage.py runserver 0.0.0.0:8000