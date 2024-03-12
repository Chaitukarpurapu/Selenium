import os
import time
from selenium import webdriver
from PIL import Image

# List of devices and resolutions to test
devices = {
    "Desktop": [
        {"width": 1920, "height": 1080},
        {"width": 1366, "height": 768},
        {"width": 1536, "height": 864}
    ],
    "Mobile": [
        {"width": 360, "height": 640},
        {"width": 414, "height": 896},
        {"width": 375, "height": 667}
    ]
}

# URL of the website to test
url = "https://www.getcalley.com/"


# Function to take screenshots
def take_screenshot(driver, folder, resolution, timestamp):
    driver.set_window_size(resolution["width"], resolution["height"])
    screenshot_name = f"{folder}/{resolution['width']}x{resolution['height']}-{timestamp}.png"
    driver.get(url)
    time.sleep(2)  # Wait for the page to load
    driver.save_screenshot(screenshot_name)


# Create folders for screenshots
def create_folders(devices):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    for device, resolutions in devices.items():
        os.makedirs(device, exist_ok=True)
        for resolution in resolutions:
            # Create driver for Chrome
            driver = webdriver.Chrome()

            # Take screenshot
            take_screenshot(driver, f"{device}", resolution, timestamp)

            # Close the driver
            driver.quit()


if __name__ == "__main__":
    try:
        create_folders(devices)
        print("Screenshots taken successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
