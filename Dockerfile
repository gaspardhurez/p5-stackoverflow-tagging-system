FROM python:3.9-slim

WORKDIR /app

COPY deployment/requirements.txt .

RUN pip install -r requirements.txt

COPY api/ /app

EXPOSE 80

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]