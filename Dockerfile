FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt .

#RUN pip install psycopg2

#RUN cat requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

#при запуске doker compose данная команда не нужна
#CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]