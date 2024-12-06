from transformers import pipeline

object_detector = pipeline(task = "object-detection", model="rnud/detr-resnet50-finetuning-watermark-pita")
objects = object_detector("data-scraping/watermarked_images/watermarked_image_0.jpg")
print(len(objects))
for obj in objects:
    print(obj)
