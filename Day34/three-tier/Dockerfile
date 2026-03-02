FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask mysql-connector-python redis
EXPOSE 8080
CMD  ["python", "app.py"]
