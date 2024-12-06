from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    status = "Incomplete"  # Default status to incomplete

    if exif_data is not None:
        model_found = False
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            if tag == "Model":
                model_found = True  # Model tag found
            print(f"{tag}: {value}")
        
        if model_found:
            status = "Complete"
    else:
        status = "No Exif Data"

    print(f"Status: {status}")
    return status

# # Example usage
# print('\nPicture from Facebook')
# get_exif_data('C:/Users/lenovo/OneDrive/Documents/PROJECTS/ALT/Real-Estate-Image-Matching/pictures/Facebook.jpg')
# print('\nPicture from FB Messenger')
# get_exif_data('C:/Users/lenovo/OneDrive/Documents/PROJECTS/ALT/Real-Estate-Image-Matching/pictures/FB Messenger.jpg')
# print('\nPicture from Google')
# get_exif_data('C:/Users/lenovo/OneDrive/Documents/PROJECTS/ALT/Real-Estate-Image-Matching/pictures/Google.jpg')
# print('\nPicture from Camera')
# get_exif_data('C:/Users/lenovo/OneDrive/Documents/PROJECTS/ALT/Real-Estate-Image-Matching/pictures/Camera.jpg')
