# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory within the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 5000 for the Flask app to listen on
EXPOSE 8082

# Run the Flask app
CMD ["python", "user_management.py"]
