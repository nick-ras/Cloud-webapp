# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY app.py ./app
COPY config.py ./
COPY .env ./

# Run app.py when the container launches
CMD "/bin/bash" "python3", "app.py"  "run" "--host" "0.0.0.0" "--port" "5000" "--reload"

