from AIDetector import classify_image 
from Watermark import check_watermark 
from Exif import get_exif_data 
import os, csv

def get_image_paths(folder_path):
    """
    Retrieves all image paths within a given folder.

    Args:
        folder_path (str): The path to the folder containing the images.

    Returns:
        list[str]: A list of image paths.
    """

    image_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                image_path = os.path.join(root, file)
                image_paths.append(image_path)
                print(image_path)
    return image_paths





ai_images = "C:/Users/lenovo/OneDrive/Documents/PROJECTS/ALT/Real-Estate-Image-Matching/dataset/ai_image_detection/test_dataset/AI Images"
authentic_images = "C:/Users/lenovo/OneDrive/Documents/PROJECTS/ALT/Real-Estate-Image-Matching/dataset/ai_image_detection/test_dataset/Authentic Images"
watermarked_images = "C:/Users/lenovo/OneDrive/Documents/PROJECTS/ALT/Real-Estate-Image-Matching/dataset/watermarked_images"
ai_image_paths = get_image_paths(ai_images)
authentic_image_paths = get_image_paths(authentic_images)
watermarked_image_paths = get_image_paths(watermarked_images)
# print(image_paths)

def determine_copyright_status(watermark_status, exif_status):
  if watermark_status == "With Watermark" or (exif_status == "Incomplete" or exif_status == "No Exif Data"):
    copyright_status = "Medium Risk"
  elif watermark_status == "With Watermark" and (exif_status == "Incomplete" or exif_status == "No Exif Data"):
    copyright_status = "High Risk"
  else:
    copyright_status = "Clear"
  return copyright_status

csv_data = []
def generate_fraud_dataset(list_of_image_paths):
    num_copyright_images = 0
    num_AI_images = 0
    num_authentic_images = 0
    percentage_copyright_images = 0
    percentage_AI_images = 0
    percentage_authentic_images = 0
    metrics = 0
    number = 0
    for count, path in enumerate(list_of_image_paths):
        ID = count
        image_path = path
        watermark_status = check_watermark(image_path)
        exif_status = get_exif_data(image_path)
        copyright_status = determine_copyright_status(watermark_status, exif_status)
        ai_status, ai, authentic = classify_image(image_path)
        
        if count > 0:
          if copyright_status != "Clear":
            num_copyright_images += 1
            percentage_copyright_images = num_copyright_images/count * 100
          if ai > authentic:
            num_AI_images += 1
            percentage_AI_images = num_AI_images/count * 100
          if authentic > ai and copyright_status == "Clear":
            num_authentic_images += 1
            percentage_authentic_images = num_authentic_images/count * 100
        
          metrics = [percentage_copyright_images, percentage_AI_images, percentage_authentic_images, 100]
          number = [num_copyright_images, num_AI_images, num_authentic_images, count]


        data = [ID, image_path, copyright_status, watermark_status, exif_status, ai, authentic]
        csv_data.append(data)
        print(data)
        # Open the CSV file for writing
        # Specify the desired folder path
        folder_path = "C:/Users/lenovo/OneDrive/Documents/PROJECTS/ALT/Real-Estate-Image-Matching/real-estate-webiste/src"
        target_dir = os.path.join(folder_path, 'fraud_dataset3.csv')
        with open(target_dir, 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            # Write the header row
            # csvwriter.writerow(['ID','Image Path', 'Copyright Status', 'Watermark Status', 'Exif Status', 'AI', 'Authentic'])
            # Write the data rows
            csvwriter.writerow(data)
        target_dir = os.path.join(folder_path, 'metrics.csv')
        with open(target_dir, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            # Write the header row
            csvwriter.writerow(['Copyright', 'AI Generated', 'Authentic', 'Total'])
            # Write the data rows
            if number:
              csvwriter.writerow(number)
            if metrics:
              csvwriter.writerow(metrics)
            
        

custom_images = "C:/Users/lenovo/OneDrive/Documents/PROJECTS/ALT/Real-Estate-Image-Matching/dataset/custom"
custom_image_paths = get_image_paths(custom_images)
# authentic_image_paths
# watermarked_image_paths
# ai_image_paths
generate_fraud_dataset(watermarked_image_paths)

