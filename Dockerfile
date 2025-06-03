FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn jinja2

EXPOSE 8080

CMD ["uvicorn", "painel:app", "--host", "0.0.0.0", "--port", "8080"]