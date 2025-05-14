from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import time
import os

def screenshot_full_scroll_and_stitch(url, output_file='stitched_fullpage.png'):
    # Headless Chrome setup
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(2)

    # Get total scroll height and viewport height
    total_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")

    num_screens = (total_height // viewport_height) + 1
    images = []

    for i in range(num_screens):
        scroll_y = i * viewport_height
        driver.execute_script(f"window.scrollTo(0, {scroll_y});")
        time.sleep(0.2)  # Let content render

        filename = f"part_{i}.png"
        driver.save_screenshot(filename)
        images.append(Image.open(filename))

    # Stitch images together
    stitched_image = Image.new('RGB', (images[0].width, sum(img.height for img in images)))
    offset = 0
    for img in images:
        stitched_image.paste(img, (0, offset))
        offset += img.height

    stitched_image.save(output_file)
    print(f"Saved full stitched screenshot to {output_file}")

    # Cleanup
    for img in images:
        img.close()
    for i in range(num_screens):
        os.remove(f"part_{i}.png")

    driver.quit()

# Example usage
if __name__ == "__main__":
    screenshot_full_scroll_and_stitch("https://example.com", "example_fullpage_stitched.png")
