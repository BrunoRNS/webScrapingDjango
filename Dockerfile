FROM mcr.microsoft.com/playwright:noble

# Disable writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Set Playwright browser path
ENV PLAYWRIGHT_BROWSERS_PATH=0

# Set app directory
WORKDIR /app

RUN apt-get install -y python3-pip python3-dev python3-virtualenv && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN virtualenv venv && \
    ./venv/bin/pip install --upgrade pip && \
    ./venv/bin/pip install -r requirements.txt && \
    ./venv/bin/playwright install chromium

COPY . .

EXPOSE 5000

CMD ["./venv/bin/gunicorn", "--bind", "0.0.0.0:5000", "--workers", "1", "--threads", "1", "--worker-class", "sync", "--log-level", "info", "app:app"]
