# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app/ .

# Set environment variables
ENV FLASK_APP=__init__.py
ENV FLASK_ENV=development

# Expose the port
EXPOSE 5000

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
