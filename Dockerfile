FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

COPY deployment/requirements.txt .

RUN apt-get update && apt-get install -y build-essential libatlas-base-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY api/ /app

EXPOSE 8181

CMD ["flask", "run", "--host=0.0.0.0", "--port=8181"]