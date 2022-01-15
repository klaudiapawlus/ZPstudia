from imageai.Detection import ObjectDetection
import os
import liczenie
import zdjecia


zdjecia.odczyt()

sciezka = os.getcwd()
sciezka2 = "output"
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(sciezka,
                                   "resnet50_coco_best_v2.1.0.h5"))
detector.loadModel()
custom = detector.CustomObjects(person=True)

for zdjecie in zdjecia.zdjecia:
    detector.detectObjectsFromImage(input_image=os.path.join(zdjecia.folder_dir, zdjecie),
                                    output_image_path=os.path.join(sciezka2, zdjecie),
                                    minimum_percentage_probability=45, custom_objects=custom)
    print(f'Jest:{liczenie.liczenie(zdjecie)} osob')

# for eachObject in detections1:
#     print(eachObject["name"], " : ", eachObject["percentage_probability"])
# for eachObject in detections2:
#     print(eachObject["name"], " : ", eachObject["percentage_probability"])
# for eachObject in detections3:
#     print(eachObject["name"], " : ", eachObject["percentage_probability"])
