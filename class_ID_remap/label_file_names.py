import os

label_folder = r"C:\Users\dinyz\Dinesh Ram\Pycharm - Projects\Wildlife Animal Detection\class_ID_remap\Elephants\train\labels"

for filename in os.listdir(label_folder):
    if filename.endswith('_jpg.txt'):
        new_filename = filename.replace('_jpg.txt', '.txt')
        os.rename(os.path.join(label_folder, filename), os.path.join(label_folder, new_filename))
        print(f"Renamed label: {filename} ➜ {new_filename}")
