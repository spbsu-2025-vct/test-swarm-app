FROM python:3.9-slim

WORKDIR /swarm-app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./swarm-app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]