import os
from ImgEntity import ImgEntity

imgEntities = []

for root, dirs, files in os.walk("./UBIRIS_200_150_R"):
    for file in files:
        filename, ext = os.path.splitext(file)
        if ext not in [".jpg"]:
            continue

        name_parts = filename.split("_")

        id = name_parts[1] + "_" + name_parts[2] + "_" + name_parts[3]
        person_id = name_parts[1]
        absolutepath = os.path.abspath(filename)

        imgEntity = ImgEntity(person_id, person_id, absolutepath)
        imgEntities.append(imgEntity)



for imgEntity in imgEntities:
    imgEntity.show_id()
