import os
import time
import requests
from selenium import webdriver
from PIL import Image
import base64

IMAGE_URL = "https://home.cady.com/wp-content/uploads/2019/04/Graduation-800.jpg"



def upload_image_to_imgbb(image_path, image_url=None, expiration=None):
    """Uploads an image to imgbb and returns the temporary URL."""

    url = "https://api.imgbb.com/1/upload"
    key = "5a4823dd9c6e40e2ba0c77aa113924ec"  # Replace with your actual imgbb API key

    if image_path:
        with open(image_path, "rb") as image:
            image_data = image.read()
            files = {'image': (image.name, image_data)}  # Include filename in form data
    elif image_url:
        files = {'image': image_url}
    else:
        raise ValueError("Either image_path or image_url must be provided.")

    payload = {'key': key}

    if expiration:
        payload['expiration'] = expiration

    response = requests.post(url, files=files, data=payload)

    if response.status_code == 200:
        data = response.json()
        image_url = data['data']['url']
        print("Image uploaded successfully:", image_url)
    else:
        print("Error uploading image:", response.text)
        image_url = None
    
    return image_url

def download_google_lens_image_results(image_url):
    url = "https://lens.google.com/uploadbyurl?url=" + image_url

    # Initialize a Firefox webdriver
    driver = webdriver.Firefox()

    # Open the webpage
    driver.get(url)

    # Wait for 5 seconds to let the page load
    time.sleep(5)

    # Execute JavaScript to get src attributes of specific elements
    elements = driver.execute_script("""
        var elements = document.getElementsByClassName("wETe9b jFVN1");
        var srcList = [];
        for (let element of elements) {
            srcList.push(element.src);
        }
        return srcList; 
    """)

    # Close the webdriver
    driver.quit()

    # Create directory to save downloaded images if it doesn't exist
    if not os.path.exists('downloaded_images'):
        os.makedirs('downloaded_images')

    # Download each image
    for index, image_url in enumerate(elements):
        try:
            response = requests.get(image_url)
            if response.status_code == 200:  
                with open(f"fraud-filter-system/copyright-image-detection/googleDuplicates/downloaded_images/image_{index}.jpg", 'wb') as f:
                    f.write(response.content)
                print(f"Image {index} downloaded successfully.")
            else:
                print(f"Failed to download image {index}: HTTP status code {response.status_code}")
        except Exception as e:
            print(f"Error downloading image {index}: {str(e)}")

    print("All images downloaded.")

image_path = "C:/Users/lenovo/OneDrive/Documents/PROJECTS/ALT/Real-Estate-Image-Matching/fraud-filter-system/copyright-image-detection/googleDuplicates/china ai.png"
image_url = upload_image_to_imgbb(image_path, 86400)

