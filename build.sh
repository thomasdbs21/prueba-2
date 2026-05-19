#!/bin/bash

cat <<EOF > Dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
EOF

docker build -t clima-app .

docker run --name samplerunning \
-e API_KEY_PROYECTO=$API_KEY_PROYECTO \
clima-app
