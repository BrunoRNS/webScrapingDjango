FROM mcr.microsoft.com/playwright:noble

# Disable writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Set Playwright browser path
ENV PLAYWRIGHT_BROWSERS_PATH=0

# Set app directory
WORKDIR /app

RUN apt-get update && apt-get install -y python3-pip python3-dev python3-virtualenv && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN virtualenv venv && \
    ./venv/bin/pip install --upgrade pip && \
    ./venv/bin/pip install -r requirements.txt && \
    ./venv/bin/playwright install chromium

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "./venv/bin/python manage.py migrate && python manage.py collectstatic --noinput && ./venv/bin/gunicorn WebScrapingDjango.wsgi:application --bind 0.0.0.0:$PORT --workers 3"]