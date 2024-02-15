FROM python:3.8

WORKDIR /app

COPY requirements.txt /app
COPY website /app/website

RUN apt-get update && \
    pip install -r requirements.txt && \
    chmod -R 777 /app && \
    chmod -R 777 /app/website

WORKDIR /app/website

EXPOSE 8000

ENTRYPOINT ["python3"]
CMD ["app.py", "runserver", "0.0.0.0:8000"]