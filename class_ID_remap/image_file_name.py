import os

image_folder = r"C:\Users\dinyz\Dinesh Ram\Pycharm - Projects\Wildlife Animal Detection\class_ID_remap\Elephants\train\images"

for filename in os.listdir(image_folder):
    if filename.endswith('_jpg'):
        new_filename = filename.replace('_jpg', '.jpg')
        os.rename(os.path.join(image_folder, filename), os.path.join(image_folder, new_filename))
        print(f"Renamed image: {filename} ➜ {new_filename}")
