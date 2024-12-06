import easyocr

def check_watermark(image_path):
    reader = easyocr.Reader(['en'])
    text = reader.readtext(image_path, detail=0)
    
    if text:
        status = "With watermark"
    else:
        status = "Clean"
    
    return status

# # Example usage
# image_path = r'C:\Users\lenovo\OneDrive\Documents\PROJECTS\ALT\Real-Estate-Image-Matching\dataset\watermarked_images\watermarked_image_2.jpg'
# status = check_watermark(image_path)
# print(f"Status: {status}")
