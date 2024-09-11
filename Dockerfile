# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /opt/app-root/src

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Specify the command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]

