# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app


COPY ./requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

COPY .env ./
# env vars set in shell
COPY entrypoint.sh ./


# Define environment variable
ENV NAME World

# Run app.py when the container launches
ENTRYPOINT ["./entrypoint.sh", "--host", "0.0.0.0", "--port", "5000", "--reload"]

