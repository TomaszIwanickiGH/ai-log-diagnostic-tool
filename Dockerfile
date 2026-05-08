FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir ollama

COPY analyzer.py .
COPY server.log .

CMD ["python", "analyzer.py"]