import os

label_folder = r"C:\Users\dinyz\Dinesh Ram\Pycharm - Projects\Wildlife Animal Detection\class_ID_remap\Normal-abnormal-elephants\train\labels"
image_folder = r"C:\Users\dinyz\Dinesh Ram\Pycharm - Projects\Wildlife Animal Detection\class_ID_remap\Normal-abnormal-elephants\train\images"
image_extensions = ['.jpg', '.jpeg', '.png']

deleted_count = 0

for label_file in os.listdir(label_folder):
    if label_file.endswith('.txt'):
        label_path = os.path.join(label_folder, label_file)

        if not os.path.exists(label_path):
            print(f"❌ Label missing: {label_file} — Skipping")
            continue

        try:
            with open(label_path, 'r') as f:
                content = f.read()
                if content.strip() == "":
                    raise ValueError("Empty file")

        except (OSError, ValueError):
            print(f"⚠️ Deleting invalid label: {label_file}")
            os.remove(label_path)

            # Delete matching image
            base_name = os.path.splitext(label_file)[0]
            image_deleted = False
            for ext in image_extensions:
                image_path = os.path.join(image_folder, base_name + ext)
                if os.path.exists(image_path):
                    os.remove(image_path)
                    print(f"🗑️ Deleted image: {base_name + ext}")
                    image_deleted = True
                    break

            if not image_deleted:
                print(f"❌ No matching image found for: {base_name}")
            deleted_count += 1

print(f"\n✅ Cleanup done. Deleted {deleted_count} label-image pairs.")
