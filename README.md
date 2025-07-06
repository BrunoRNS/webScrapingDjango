# SPA Static Downloader (webScrapingDjango)

**SPA Static Downloader** is a Django web application that lets you generate static, downloadable ZIP archives of JavaScript-heavy Single Page Applications (SPAs) like those built with React, Vue, Angular, or Svelte. It uses Playwright to render the site in a real browser (Firefox), downloads all assets (HTML, CSS, JS, images, fonts), and packages everything for easy hosting on platforms like Netlify or GitHub Pages.

---

## Use it Online

### Usage

**To access this website hosted with _render_ visit [SPA Static Downloader](.)**

### Security

> Note: hosted with extremely security, configured using reCAPTCHA, csrf_token, ratelimit, environment variables and much more security tools.

---

## 🚀 Features

- **SPA to Static**: Converts any public SPA URL into a static site.
- **Full Asset Download**: Grabs HTML, CSS, JS, images, and fonts.
- **Browser Rendering**: Uses Playwright with Firefox for accurate JS rendering.
- **reCAPTCHA Protection**: Prevents abuse with Google reCAPTCHA.
- **Rate Limiting**: Protects endpoints from excessive requests.
- **Ready-to-Host ZIP**: Download a ZIP file ready for deployment.
- **Modern UI**: Simple, responsive interface with dark/light mode.

---

## 🛠️ Quick Start

1. **Clone the repository:**

   ```bash
   git clone https://github.com/BrunoRNS/webScrapingDjango.git
   cd webScrapingDjango
   ```

2. **Run the setup script:**

   ```bash
   bash setup.sh
   ```

3. **Configure environment variables:**

   - Edit `.env` (generated from `.env-example`) with your Django secret key and reCAPTCHA keys.

4. **Start the server:**

   ```bash
   source venv/bin/activate
   python manage.py runserver
   ```

5. **Open your browser:**  
   Visit [http://localhost:8000](http://localhost:8000)

---

## 📝 Usage

1. Enter the URL of the SPA site you want to download.
2. Complete the reCAPTCHA.
3. Click **Generate ZIP**.
4. Download your static site archive!

---

## ⚙️ Tech Stack

- **Backend:** Django 5, Playwright, BeautifulSoup, Requests
- **Frontend:** HTML, CSS, JavaScript
- **Security:** Google reCAPTCHA, django-ratelimit

---

## 📄 License

This project is licensed under the [GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.html).

---

## 🙋‍♂️ Author

Made by [BrunoRNS](https://github.com/BrunoRNS)
