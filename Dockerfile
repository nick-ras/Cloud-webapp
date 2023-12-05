# Use an official Python runtime as a parent image
FROM python:3.8-slim


WORKDIR /app
# Install system dependencies

RUN useradd -m dockeruser

USER root

RUN apt-get update -y && apt-get install -y \
	apt-utils \
	build-essential \
	unixodbc \
	unixodbc-dev \
	curl 

RUN apt-get update
RUN apt-get install -y curl gnupg
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl -sSL https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18

COPY . /app
# COPY odbcinst.ini /etc/
# COPY odbc.ini /etc/

#install needed packages from req.txt
RUN pip install --no-cache-dir -r requirements.txt

# Clean up unnecessary files
RUN apt-get clean

USER dockeruser
# Run app.py when the container launches
ENTRYPOINT ["python3", "app.py",  "run", "--host", "0.0.0.0", "--port", "8080", "--reload"]
