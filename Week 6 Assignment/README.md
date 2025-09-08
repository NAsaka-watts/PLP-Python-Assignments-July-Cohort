# Ubuntu Image Fetcher

A mindful image downloader inspired by Ubuntu's philosophy:
> "I am because we are."

This tool connects you to the global community by respectfully fetching images from the web and organizing them for later sharing.

---

## Features
- Download one or more images from URLs
- Gracefully handle network and HTTP errors
- Validate images using the `Content-Type` header
- Skip duplicate images to avoid overwriting
- Organize downloads into a `Fetched_Images` directory

---

## Requirements
- Python 3.x
- `requests` library

Install requirements with:
```bash
pip install requests