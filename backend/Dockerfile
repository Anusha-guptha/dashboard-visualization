# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory inside the container to the api folder
WORKDIR /app/api

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run manage.py when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


