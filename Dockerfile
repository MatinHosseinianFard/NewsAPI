FROM python:3.10-slim

# Set the working directory inside the container to /code
WORKDIR /code

# Copy the requirements file into the container at /code/
COPY requirements.txt /code/

RUN pip install -U pip

RUN pip install -r requirements.txt

# Copy the entire project directory into the container at /code/
COPY . /code/

# Expose port 8000 for the application to listen on
EXPOSE 8000

# Define the command to run the application using Gunicorn
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
