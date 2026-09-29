# OpenRepair — Flask app served by gunicorn
FROM python:3.12-slim

WORKDIR /app

# Install dependencies first to reuse the cached layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# 3 gunicorn workers; each request opens and closes its MySQL connection
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "app:app"]
