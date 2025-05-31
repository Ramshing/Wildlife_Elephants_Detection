import os

# Remap dictionary {old_id: new_id}
folder1_remap = {0:1}
# folder2_remap = {0: 3, 1: 4, 2: 5, 3:6}

def remap_labels(folder_path, remap_dict):
    for file in os.listdir(folder_path):
        if file.endswith('.txt'):
            file_path = os.path.join(folder_path, file)

            if not os.path.isfile(file_path):
                print(f"❌ File not found: {file_path}")
                continue  # Skip missing files to avoid crash

            with open(file_path, 'r') as f:
                lines = f.readlines()
            new_lines = []
            for line in lines:
                parts = line.strip().split()
                old_id = int(parts[0])
                new_id = remap_dict[old_id]
                parts[0] = str(new_id)
                new_lines.append(' '.join(parts) + '\n')
            with open(file_path, 'w') as f:
                f.writelines(new_lines)

# Run for both folders
#remap_labels(r'C:\Users\dinyz\Dinesh Ram\Pycharm - Projects\Wildlife Animal Detection\class_ID_remap\Normal-abnormal-elephants_labels\train\labels_valid', folder1_remap)
remap_labels(r'C:\Users\dinyz\Dinesh Ram\Pycharm - Projects\Wildlife Animal Detection\class_ID_remap\Road side elephants\valid\labels', folder1_remap)
