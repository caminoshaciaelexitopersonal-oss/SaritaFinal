from playwright.sync_api import sync_playwright
import os
import time

def run():
    os.makedirs("jules-scratch/verification", exist_ok=True)
    urls = [
        {"path":"home", "url":"http://localhost:3000/"},
        {"path":"registro", "url":"http://localhost:3000/registro"},
        {"path":"login", "url":"http://localhost:3000/login"},
        {"path":"prestador-registro", "url":"http://localhost:3000/auth/registration/prestador"},
    ]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for item in urls:
            try:
                print(f"-> Capturando {item['url']}")
                # Using networkidle is crucial for SPAs
                page.goto(item["url"], wait_until="networkidle")
                # Wait for a key element that confirms the page is rendered
                page.wait_for_selector('header', timeout=30000)
                screenshot_path = f"jules-scratch/verification/{item['path']}.png"
                page.screenshot(path=screenshot_path, full_page=True)
                print(f"   Screenshot guardado en: {screenshot_path}")
            except Exception as e:
                print(f"   Error capturando {item['url']}: {e}")
        browser.close()

if __name__ == "__main__":
    run()
