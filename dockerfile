# Dockerfile
FROM python:3.9

WORKDIR /app

# Copy application code
COPY app.py /app/
COPY gunicorn_config.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the application will run
EXPOSE 5000

# Command to run the application
CMD ["gunicorn", "app:app", "-c", "./gunicorn_config.py"]
