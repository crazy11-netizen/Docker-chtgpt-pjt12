# Base Image
FROM python:3.12-slim

# Working Directory
WORKDIR /app

# Install system packages required by mysqlclient
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Copy dependency file first (better Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . .

# Expose application port
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
