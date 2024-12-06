import piexif , random, datetime
from PIL import Image
from PIL.ExifTags import TAGS
from os import listdir
from os.path import isfile, join


filename = r"C:\Users\lenovo\OneDrive\Documents\PROJECTS\ALT\Real-Estate-Image-Matching\data-augmentation\images\listing_1_image_1.png_20240927_174704.jpg"


make_models = [
    ("Samsung", "Galaxy A54"),
    ("Samsung", "Galaxy A34"),
    ("Samsung", "Galaxy A14"),
    ("Samsung", "Galaxy S23"),
    ("Samsung", "Galaxy S23+"),
    ("Samsung", "Galaxy S23 Ultra"),
    ("iPhone", "iPhone 13"),
    ("iPhone", "iPhone 14"),
    ("iPhone", "iPhone 14 Plus"),
    ("iPhone", "iPhone 14 Pro"),
    ("iPhone", "iPhone 14 Pro Max"),
    ("Xiaomi", "Redmi Note 12"),
    ("Xiaomi", "Redmi Note 12 Pro"),
    ("Xiaomi", "Redmi Note 12 Pro+"),
    ("Xiaomi", "Redmi Note 12 Turbo"),
    ("OPPO", "Reno8"),
    ("OPPO", "Reno8 Pro"),
    ("OPPO", "A78"),
    ("OPPO", "A58"),
    ("Vivo", "V27"),
    ("Vivo", "V27 Pro"),
    ("Vivo", "Y36"),
    ("Vivo", "Y35"),
    ("Realme", "C55"),
    ("Realme", "C33"),
    ("Realme", "10 Pro 5G"),
    ("Realme", "10 Pro+ 5G"),
    # Add more device models as needed
]
def add_exif_data(filename):
    listing_number = filename.split("_")[1]
    exif_dict = piexif.load(filename)
    random_datetime = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 365))
    if listing_number in exif_data:
        exif_dict = exif_data[listing_number].copy()
    else:
        random_device = random.choice(make_models)
        exif_dict["0th"][piexif.ImageIFD.Make] = random_device[0]
        exif_dict["0th"][piexif.ImageIFD.Model] = random_device[1]
        exif_dict["0th"][piexif.ImageIFD.Software] =  "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=13))
        exif_dict["0th"][piexif.ImageIFD.DateTime] = random_datetime.strftime("%Y:%m:%d %H:%M:%S")
        exif_data[listing_number] = exif_dict

    with Image.open(filename) as img:
        exif_dict["0th"][piexif.ImageIFD.ImageWidth] = img.width
        exif_dict["0th"][piexif.ImageIFD.ImageLength] = img.height

    
    

    exif_dict["0th"][piexif.ImageIFD.YCbCrPositioning] = 1
    exif_dict["0th"][piexif.ImageIFD.Orientation] = 1
    exif_dict["0th"][piexif.ImageIFD.ResolutionUnit] = 2
    exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = random_datetime.strftime("%Y:%m:%d %H:%M:%S")
    exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = random_datetime.strftime("%Y:%m:%d %H:%M:%S")
    exif_dict["Exif"][piexif.ExifIFD.Flash] = random.randint(0, 1)
    exif_dict["Exif"][piexif.ExifIFD.FocalLengthIn35mmFilm] = random.randint(24, 200)
    exif_dict["Exif"][piexif.ExifIFD.SceneCaptureType] = 0
    exif_dict["Exif"][piexif.ExifIFD.OffsetTime] = b"+08:00"
    exif_dict["Exif"][piexif.ExifIFD.OffsetTimeOriginal] = b"+08:00"
    exif_dict["Exif"][piexif.ExifIFD.ImageUniqueID] = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=16))
    exif_dict["Exif"][piexif.ExifIFD.ExposureProgram] = random.randint(0, 8)
    exif_dict["Exif"][piexif.ExifIFD.ISOSpeedRatings] = 2 ** random.randint(0, 10)
    exif_dict["Exif"][piexif.ExifIFD.ExposureMode] = random.randint(0, 2)
    exif_dict["Exif"][piexif.ExifIFD.WhiteBalance] = random.randint(0, 4)

    # Save the image with modified EXIF data
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, filename)
    return 


# Folder path containing images
folder_path = r"C:\Users\lenovo\OneDrive\Documents\PROJECTS\ALT\Real-Estate-Image-Matching\data-scraping\authentic\2. add exif data\authentic_results"

# Get all image files in the folder
image_files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

exif_data = {}
# Process each image file
for image in image_files:
    print(image)
    add_exif_data(join(folder_path, image))



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

for image in image_files:
    print('\nPicture')
    get_exif_data(join(folder_path, image))
    print("\n")
