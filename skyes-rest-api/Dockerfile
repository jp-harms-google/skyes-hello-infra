FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY skyes-rest-api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /skyes-rest-api
COPY skyes-rest-api ./skyes-rest-api

CMD ["uvicorn", "skyes-rest-api.main:app", "--host", "0.0.0.0", "--port", "8080"]