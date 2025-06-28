# SPA Static Downloader (webScrapingDjango) Documentation

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture Overview](#architecture-overview)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Guide](#usage-guide)
- [Security](#security)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [API & Internal Modules](#api--internal-modules)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Author](#author)

---

## Introduction

**SPA Static Downloader** is a Django-based web application that converts JavaScript-heavy Single Page Applications (SPAs) into static, downloadable ZIP archives. It leverages Playwright for browser automation, ensuring accurate rendering of modern web apps, and packages all assets (HTML, CSS, JS, images, fonts) for easy deployment on static hosting platforms.

---

## Features

- **SPA to Static**: Converts any public SPA (React, Vue, Angular, Svelte, etc.) into a static site.
- **Full Asset Download**: Captures HTML, CSS, JS, images, and fonts.
- **Browser Rendering**: Uses Playwright (Chromium) for real browser rendering.
- **Security**: Integrates Google reCAPTCHA, CSRF protection, and rate limiting.
- **Ready-to-Host ZIP**: Generates a ZIP archive ready for Netlify, GitHub Pages, etc.
- **Modern UI**: Responsive interface with dark/light mode.
- **Automated Cleanup**: Temporary files are cleaned up automatically.

---

## Architecture Overview

- **Backend**: Django 5, Playwright, BeautifulSoup, Requests
- **Frontend**: HTML, CSS, JavaScript
- **Security**: Google reCAPTCHA, django-ratelimit, CSRF tokens
- **Utilities**: Automated temporary directory cleaner

---

## Installation

### Prerequisites

- Python 3.8+
- Git
- [Playwright Browsers](https://playwright.dev/python/docs/browsers)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/BrunoRNS/webScrapingDjango.git
   cd webScrapingDjango
   ```

2. **Run the setup script:**

   ```bash
   bash setup.sh
   ```

3. **Activate the environment created by setup.sh:**

   ```bash
   source ./venv/bin/activate
   ```

4. **Configure environment variables:**
   - Edit `.env` (generated from `.env-example`) with your Django secret key and reCAPTCHA keys.

5. **Start the server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the app:**
   - Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## Configuration

- **Environment Variables** (`.env`):
  - `DEBUG`: Set to `True` for development, `False` for production.
  - `DJANGO_SECRET_KEY`: Your Django secret key.
  - `RECAPTCHA_PRIVATE_KEY` / `RECAPTCHA_PUBLIC_KEY`: Google reCAPTCHA keys.

- **Dependencies**: Listed in `requirements.txt`.

---

## Usage Guide

1. **Home Page**: Enter the SPA URL, complete the reCAPTCHA, and click "Generate ZIP".
2. **Download**: After processing, a ZIP file containing the static site will be downloaded.
3. **Hosting**: Extract and deploy the ZIP contents to any static hosting provider.

---

## Security

- **reCAPTCHA**: Prevents automated abuse.
- **Rate Limiting**: Limits requests per IP (5/s for views, 2/s for downloads).
- **CSRF Protection**: Enabled by default in Django.
- **Environment Variables**: Sensitive keys are not hardcoded.
- **Temporary File Cleanup**: Old files are deleted automatically.

---

## Testing

- **Run all tests:**

  ```bash
  bash tests/runTests.sh
  ```

- **Continuous Integration**: GitHub Actions workflow in `.github/workflows/django.yml` runs tests on push and pull requests.

---

## Project Structure

```sh
webScrapingDjango/
├── core/
│   ├── middleware/
│   ├── spa_downloader/
│   ├── utils/
│   └── apps/
├── home/
│   ├── forms/
│   ├── static/
│   ├── templates/
│   └── views/
├── tests/
├── WebScrapingDjango/   # Django project settings
├── manage.py
├── requirements.txt
├── setup.sh
├── .env-example
└── README.md
```

---

## API & Internal Modules

### Main Components

- **SPA Downloader** (`core/spa_downloader/spa_downloader.py`)
  - Class: `SPAStaticDownloader`
  - Methods:
    - `download()`: Renders the SPA, extracts assets, saves locally.
- **Temporary Cleaner** (`core/utils/tmp_cleaner.py`)
  - Deletes old temporary folders asynchronously.
- **Middleware** (`core/middleware/TMPcleaner.py`)
  - Runs the cleaner on each request.
- **Forms** (`home/forms/forms.py`)
  - `UrlForm`: Handles URL input and reCAPTCHA.
- **Views** (`home/views/`)
  - `home.py`: Home page.
  - `about.py`: About page.
  - `file_downloader.py`: Handles SPA download and ZIP creation.

---

## Troubleshooting

- **Playwright Errors**: Ensure browsers are installed (`playwright install chromium`).
- **reCAPTCHA Issues**: Check your keys in `.env`.
- **Permission Errors**: Ensure the app has write access to the `tmp/` directory.
- **Dependencies**: Reinstall with `pip install -r requirements.txt`.

---

## License

This project is licensed under the [GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.html).

---

## Author

Made by [BrunoRNS](https://github.com/BrunoRNS)
