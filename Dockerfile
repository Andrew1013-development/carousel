FROM python:3.13.1

WORKDIR /app
COPY /app/blueprints/ blueprints/
COPY /app/__init__.py __init__.py
COPY /requirements.txt requirements.txt
COPY /app/.env .env
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", ".", "run", "--host", "0.0.0.0"]