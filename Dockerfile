# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Install ODBC libraries
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev

# Install FreeTDS (optional, but may be needed for SQL Server)
RUN apt-get install -y freetds-dev freetds-bin

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# COPY ./src ./src
# COPY app.py ./app
# COPY config.py ./
COPY . ./

# Run app.py when the container launches
ENTRYPOINT ["python3", "app.py",  "run", "--host", "0.0.0.0", "--port", "5000", "--reload"]

