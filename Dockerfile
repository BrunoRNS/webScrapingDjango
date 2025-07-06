FROM mcr.microsoft.com/playwright:noble

# Disable writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Set Playwright browser path
ENV PLAYWRIGHT_BROWSERS_PATH=0

# Set app directory
WORKDIR /app

# Update package list and install basic development tools
RUN apt-get update && apt-get install -y python3-pip python3-dev python3-virtualenv build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN virtualenv venv

RUN source ./venv/bin/activate

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    playwright install chromium

# Copy all application code
COPY . .

# Expose port for Flask
EXPOSE 5000

# Command to run with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "--threads", "1", "--worker-class", "sync", "--log-level", "info", "app:app"]

