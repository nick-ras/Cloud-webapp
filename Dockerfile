# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
	unixodbc-dev \
	&& rm -rf /var/lib/apt/lists/*

# Install ODBC libraries
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# COPY ./src ./src
# COPY app.py ./app
# COPY config.py ./
COPY . ./

# Run app.py when the container launches
ENTRYPOINT ["python3", "app.py",  "run", "--host", "0.0.0.0", "--port", "8080", "--reload"]

