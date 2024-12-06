from PIL import Image
import os

def convert_png_to_jpg(input_folder, output_folder):
  """Converts all PNG images in the input folder to JPG format and saves them in the output folder.

  Args:
    input_folder: Path to the input folder containing PNG images.
    output_folder: Path to the output folder where JPG images will be saved.
  """

  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
      input_path = os.path.join(input_folder, filename)
      output_path = os.path.join(output_folder, filename[:-4] + ".jpg")

      with Image.open(input_path) as img:
        img.save(output_path, "JPEG")

# Example usage:
input_folder = r"data-scraping\authentic\1. convert to PNG\png"
output_folder = r"C:\Users\lenovo\OneDrive\Documents\PROJECTS\ALT\Real-Estate-Image-Matching\data-scraping\authentic\1. convert to PNG\png"
convert_png_to_jpg(input_folder, output_folder)