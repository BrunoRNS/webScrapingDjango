from playwright.sync_api import sync_playwright
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from bs4 import Tag
import requests
import os

SUPPORTED_BROWSERS = ["firefox"]

class SPAStaticDownloader:
    
    def __init__(
        
        self, 
        url: str, 
        output_dir: str = "output", 
        browser: str = "chromium", 
        headless: bool = True,
        
    ):
        
        self.url = url
        self.output_dir = output_dir
        self.browser_name = browser.lower()
        self.headless = headless

        if self.browser_name not in SUPPORTED_BROWSERS:
            
            raise ValueError(f"Unsupported browser: {self.browser_name}. Choose from {SUPPORTED_BROWSERS}")

    def _save_html(self, html: str):
        
        os.makedirs(self.output_dir, exist_ok=True)
        path = os.path.join(self.output_dir, "index.html")
        
        with open(path, "w", encoding="utf-8") as f:
            
            f.write(html)
            
        print(f"[✓] HTML saved to {path}")


    def _download_asset(self, url: str):
        
        try:
            
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                
                parsed = urlparse(url)
                local_path = os.path.join(self.output_dir, parsed.netloc + parsed.path)
                
                if local_path.endswith("/"):
                    local_path += "index.html"
                    
                os.makedirs(os.path.dirname(local_path), exist_ok=True)
                
                with open(local_path, "wb") as f:
                    f.write(response.content)
                    
                print(f"[✓] Asset saved: {local_path}")
                
        except Exception as e:
            
            print(f"[✗] Failed to download {url}: {e}")

    def _extract_assets(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        urls = set()
        

        for tag in soup.find_all(["link", "script", "img"]):
            
            if not isinstance(tag, Tag):
            
                continue
            
            attr = None

            if tag.name == "link":
                attr = tag.get("href")
            elif tag.name in ("script", "img"):
                attr = tag.get("src")

            if attr != None:
                
                full_url = urljoin(self.url, str(attr))
                
                if full_url.startswith("http"):
                    
                    urls.add(full_url)

        return urls

    def download(self):
        
        print(f"[→] Launching browser: {self.browser_name}")
        
        with sync_playwright() as p:
            
            browser_launcher = getattr(p, self.browser_name)
            browser = browser_launcher.launch(headless=self.headless)
            page = browser.new_page()
            page.goto(self.url, wait_until="networkidle")

            html = page.content()
            self._save_html(html)

            assets = self._extract_assets(html)
            
            print(f"[→] Found {len(assets)} assets to download...")
            
            for asset_url in assets:
                
                self._download_asset(asset_url)

            browser.close()
            print(f"\n✅ Done! Static site saved to: {os.path.abspath(self.output_dir)}")
