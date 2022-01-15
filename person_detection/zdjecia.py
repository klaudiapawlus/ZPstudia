import os
folder_dir = "input"
zdjecia=[]
def odczyt():
    for images in os.listdir(folder_dir):

        if (images.endswith(".png") or images.endswith(".jpg")\
                or images.endswith(".jpeg")):
            zdjecia.append(images)
    return zdjecia

print(zdjecia)