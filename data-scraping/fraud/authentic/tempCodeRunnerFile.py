def add_exif_data(filename):
    listing_number = filename.split("_")[1]
    exif_dict = piexif.load(filename)
    random_datetime = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 365))
    
    if listing_number in exif_data:
        exif_dict = exif_data[listing_number].copy()
        datetime = exif_data["previous_datetime"] + datetime.timedelta(seconds=5)
        exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = datetime.strftime("%Y:%m:%d %H:%M:%S")

    else:
        random_device = random.choice(make_models)
        exif_dict["0th"][piexif.ImageIFD.Make] = random_device[0]
        exif_dict["0th"][piexif.ImageIFD.Model] = random_device[1]
        exif_dict["0th"][piexif.ImageIFD.Software] =  "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=13))
        exif_dict["0th"][piexif.ImageIFD.DateTime] = random_datetime.strftime("%Y:%m:%d %H:%M:%S")
        # Store data for this listing number
        exif_data[listing_number] = {
            "exif_dict": exif_dict,
            "previous_datetime": random_datetime
        }