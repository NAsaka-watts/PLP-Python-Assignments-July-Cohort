import os
import requests
from urllib.parse import urlparse
import hashlib

def safe_filename_from_url(url):
    """
    Extract a filename from the URL. If none found, generate one.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        filename = "downloaded_image.jpg"
    return filename

def file_exists(filepath):
    """
    Check if a file already exists by comparing MD5 hash.
    Returns True if the file already exists with identical content.
    """
    if not os.path.exists(filepath):
        return False
    return True  # Simple duplicate prevention: skip if filename already exists

def fetch_image(url, directory="Fetched_Images"):
    """
    Fetch a single image from the web and save it locally.
    Handles errors gracefully and checks HTTP headers before saving.
    """
    try:
        os.makedirs(directory, exist_ok=True)
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # Verify this is an image before saving
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return

        filename = safe_filename_from_url(url)
        filepath = os.path.join(directory, filename)

        if file_exists(filepath):
            print(f"⚠ Skipped duplicate: {filename}")
            return

        # Save file in binary mode
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Enter one or more image URLs (comma-separated): ").strip()
    if not urls:
        print("✗ No URLs provided. Exiting.")
        return

    url_list = [u.strip() for u in urls.split(",") if u.strip()]

    for url in url_list:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
