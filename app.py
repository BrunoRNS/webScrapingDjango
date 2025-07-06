from core.spa_downloader.spa_downloader import SPAStaticDownloader
from flask import Flask, request, jsonify
from urllib.parse import urlparse
from pathlib import Path
import tempfile
import base64
import validators
import logging
import re

app = Flask(__name__)

URL_REGEX = re.compile(
    r'^(https://)'
    r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,6})'
    r'(:\d+)?'
    r'(/[\w./?%&=-]*)?$'
)


def is_safe_url(url):
    """
    Checks if a URL is safe to be used by the SPA Static Downloader.

    A URL is considered safe if it is a valid URL and does not point to a
    private IP address or localhost.

    Args:
        url (str): The URL to check.

    Returns:
        bool: Whether the URL is safe.
    """
    
    if not validators.url(url):
        
        return False
    
    if not URL_REGEX.match(url):
        
        return False

    parsed = urlparse(url)
    
    if parsed.hostname in ("localhost", "127.0.0.1", "::1"):
        
        return False

    private_ip_prefixes = (
        "10.", "172.16.", "172.17.", "172.18.", "172.19.",
        "172.20.", "172.21.", "172.22.", "172.23.", "172.24.",
        "172.25.", "172.26.", "172.27.", "172.28.", "172.29.",
        "172.30.", "172.31.", "192.168."
    )
    
    if any(parsed.hostname.startswith(prefix) for prefix in private_ip_prefixes):
        
        return False

    return True

@app.route("/download-spa", methods=["POST"])
def download_spa():
    """
    Download a static copy of a Single Page App (SPA) as a JSON object containing
    base64-encoded files.

    The input should be a JSON object with a single key-value pair, where the key
    is "input_url" and the value is the URL of the SPA to download.

    The response will be a JSON object with the same structure as the input, but
    with values that are base64-encoded strings representing the contents of the
    file at the corresponding path.

    For example, if the input is `{"input_url": "https://example.com"}`, the
    response might be:

    {
        "index.html": "BASE64_ENCODED_STRING",
        "style.css": "BASE64_ENCODED_STRING",
        "script.js": "BASE64_ENCODED_STRING",
    }

    If any errors occur during the download process, the response will be a JSON
    object with a single key-value pair, where the key is "error" and the value
    is a string describing the error.
    """
    
    try:
        
        data = request.get_json(force=True, silent=True)
        
        if not data or "input_url" not in data:
            
            return jsonify({"error": "Missing 'input_url'"}), 400

        input_url = data["input_url"]
        
        if not is_safe_url(input_url):
            
            return jsonify({"error": "Invalid or unsafe URL"}), 400

        with tempfile.TemporaryDirectory() as tmpdir:
            
            downloader = SPAStaticDownloader(
                url=input_url,
                output_dir=tmpdir,
                browser="chromium",
                headless=True
            )
            
            downloader.download()

            output = {}
            
            for path in Path(tmpdir).rglob("*"):
                
                if path.is_file():
                    
                    rel_path = path.relative_to(tmpdir)
                    
                    with open(path, "rb") as f:
                        
                        encoded = base64.b64encode(f.read()).decode("utf-8")
                        output[str(rel_path)] = encoded

            return jsonify(output), 200

    except Exception as e:
        
        logging.exception("Error in /download-spa")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
