'''import os

# Folder paths
image_folder = r"C:\Users\dinyz\Dinesh Ram\Pycharm - Projects\Wildlife Animal Detection\class_ID_remap\Normal-abnormal-elephants\train\images"
label_folder = r"C:\Users\dinyz\Dinesh Ram\Pycharm - Projects\Wildlife Animal Detection\class_ID_remap\Normal-abnormal-elephants\train\labels"

# Long merged string (paste yours here)
merged_filenames =(

"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-10_jpg.rf.04822e391ecc09bac7f47032501ae204.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-19_jpg.rf.314eb39b4e61cac926f52ae14c977137.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-1_jpg.rf.8da2d4d190c5366f199076b48b25763d.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-2_jpg.rf.56d75ff51de4a41a592e5cec2adf46f3.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-36_jpg.rf.bc3d219f090791cb4ffeec0554ae0801.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-3_jpg.rf.14e06ba0787a1659966fbaf943953436.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-46_jpg.rf.c4500671fdd5d01c5c520b0e29a22fbe.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-48_jpg.rf.1b6b4b9a759758bd17a916f2f3a97c3b.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-4_jpg.rf.8d2ca0bc41d4922053ca7df866fb991c.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-50_jpg.rf.c4e4c9dde8b88473c3496d5989cb1156.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-55_jpg.rf.79ba6b8b8d5b9b9aed33ccfb6a977cdd.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-64_jpg.rf.42084dde3150b1f575657d19cf345f48.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-66_jpg.rf.704f7e6a14994e0fac7423ef99f44b17.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-6_jpg.rf.742903c8db43a011cfb2affedb114e18.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-72_jpg.rf.437e8a6c938d1f88dfbb8f5f10b4731b.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-75_jpg.rf.ece77cb7fc97c8a87b1e5d9062e418d1.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-78_jpg.rf.ba7b00fc4a9714207b46a274dc741ed4.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-9_jpg.rf.2d88d111101807f34a86c87eaae34284.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-10_jpg.rf.a84f681ce5f574f8a219fb615688b68f.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-16_jpg.rf.fb9facfeb14642638ca3215b63d1f971.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-17_jpg.rf.47ca21500b5fc7c932e6d85258579b7c.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-21_jpg.rf.cf3584c47df311e28e8445ccc4fa5b9d.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-22_jpg.rf.8d5861d1fe0646c054f48ea47bb891d7.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-23_jpg.rf.b0117951e591e5e2dedb81b19e29a303.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-27_jpg.rf.c26ff5e61d9d78bb053994ddc9d3ccb7.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-29_jpg.rf.7d736a8bfb9bc94bc47261104d33aa0e.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-30_jpg.rf.3d0a5365ebf170e0566581ee4a36819c.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-31_jpg.rf.41f0a2f90c1d8633674931588d3be950.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-33_jpg.rf.5c706aa0e908c887f2938e2e14163d88.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-35_jpg.rf.f16b54a022a24c5ec887ee1faa20cdf1.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-38_jpg.rf.49163f1c085b698af6b567df50c7bc2b.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-3_jpg.rf.501ae387012d737b50a78cc6e221ec94.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-41_jpg.rf.5031124e1ddcada03904d4db295c86b2.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-5_jpg.rf.7c6aee66fa61543e66eaed897e64e988.txt"
 "20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-10_jpg.rf.46f235297413ce8aa9a4f0b17db9ee13.txt "
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-11_jpg.rf.0e1473e775fc176a438cbbd76d0878a5.txt "
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-12_jpg.rf.259c8cc1cae5c798314c1d03bdb1a95a.txt"
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-15_jpg.rf.5980d44c809fcf778191198e704336d2.txt "
 "20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-18_jpg.rf.ef5ffd6a2c0a5fac2c2ead83d88cfcc2.txt "
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-19_jpg.rf.f57a20452934e371bf3d4e1679d63279.txt" 
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-1_jpg.rf.3223e96ac10081148b056cd5b7d32f1f.txt "
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-23_jpg.rf.336acb4f31c4fa212ae57932844655d9.txt" 
 "20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-2_jpg.rf.bdebbeefa0feb545681cbc1bb3c5d380.txt "
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-30_jpg.rf.c8f8ee4e6ed7d535f50a318a8f76a085.txt "
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-34_jpg.rf.23d7d3b60bd0bd6a6ca54e8bb3c27547.txt "
 "20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-44_jpg.rf.1b226e37ebc784264e544d9ee952e9d7.txt" 
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-9_jpg.rf.d0f2ab352391375d0a4593dde83f80a1.txt "
 "23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-13_jpg.rf.52dfa99f82e0691209f1132f9fa01a58.txt "
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-15_jpg.rf.3b3e75fd78bc677f14cf1d195d64cc96.txt "
 "23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-17_jpg.rf.2d24f15142c9ea1095273184a6ab5fd2.txt "
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-20_jpg.rf.6f1963f4c1f27d78f3c6d7a88c9f2f75.txt "
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-23_jpg.rf.b173ac6cbedb7c50346740b312bf4b24.txt "
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-26_jpg.rf.dfd51aaaba99c955ec64978d7e1a88bc.txt "
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-28_jpg.rf.2442f0ab44b1dad46cb58b5c3ad24e2a.txt" 
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-2_jpg.rf.c656af16de3557304f4047890155ed5f.txt "
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-31_jpg.rf.37777e448b6ced5d2594694856f69983.txt "
 "23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-38_jpg.rf.c8cd15868fb50c8e634b863bb522b423.txt "
 "23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-3_jpg.rf.30613ab58828b846af6d5457c80ad90c.txt"
 "23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-41_jpg.rf.cec17d1f9e1f80633ac31de2c94aab74.txt"
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-43_jpg.rf.32502c4789279b1825100fa159813dad.txt "
 "23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-4_jpg.rf.0804b01d2e85d8215c63904619c9e47a.txt"
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-6_jpg.rf.09b03a2b9d7ccd4534dede0031c06204.txt "
 "64-elephant-on-musth-aggressive-behaviour-due-to-over-secretion-of-testosterone-please-subscribe-frame-3_jpg.rf.188956bdd32164c9ec28e7407f09082d.txt "
" 80-fight-between-elephant-or-rhinoceros-elephant-Y-VS-rhinoceros-__-animal-life-animallife-1-frame-0_jpg.rf.a956de8af2cc76c020130c0aca5795bc.txt "
"80-fight-between-elephant-or-rhinoceros-elephant-Y-VS-rhinoceros-__-animal-life-animallife-1-frame-3_jpg.rf.7460afb7b4abc63e65e95a93ae16a0d1.txt "
 "80-fight-between-elephant-or-rhinoceros-elephant-Y-VS-rhinoceros-__-animal-life-animallife-1-frame-5_jpg.rf.7485a0c404b476c75bd0198a079bb19e.txt "
 "93-Big-Elephant-_-Biggar-Elephant-_-Biggest-Tusker-_-Big-Wild-Elephant-_-Biggest-Elephant-in-the-world-frame-3_jpg.rf.8a7e6e4c97943f4eb22bf6d67822f577.txt "
 "93-Big-Elephant-_-Biggar-Elephant-_-Biggest-Tusker-_-Big-Wild-Elephant-_-Biggest-Elephant-in-the-world-frame-4_jpg.rf.44aa9e7f2e3a78c94141978903b4115a.txt"
 "93-Big-Elephant-_-Biggar-Elephant-_-Biggest-Tusker-_-Big-Wild-Elephant-_-Biggest-Elephant-in-the-world-frame-7_jpg.rf.ef0f80a19f9577424e27228256611327.txt "
 "MhoJae-begins-to-relax-in-SookSai-s-presence-and-they-care-for-Sa-Ngae-together-a-i-frame-2_jpg.rf.cf51b95ff3302c0e6393e35803ceba5a.txt "
 "MhoJae-begins-to-relax-in-SookSai-s-presence-and-they-care-for-Sa-Ngae-together-a-i-frame-6_jpg.rf.4ea6b5c629502cc6f8551e5e1449c7b9.txt "
 "MhoJae-begins-to-relax-in-SookSai-s-presence-and-they-care-for-Sa-Ngae-together-a-i-frame-8_jpg.rf.cf017f45e06b2c9f399f7e0434fbb4b6.txt "
)

# Split the filenames
filenames = [line.strip() for line in merged_filenames.strip().split("\n") if line.strip()]

deleted_images = 0
deleted_labels = 0

for label_file in filenames:
    label_path = os.path.join(label_folder, label_file)
    base_name = os.path.splitext(label_file)[0]
    image_path_jpg = os.path.join(image_folder, base_name + ".jpg")

    # Delete image if it exists
    if os.path.exists(image_path_jpg):
        os.remove(image_path_jpg)
        print(f"🗑️ Deleted image: {image_path_jpg}")
        deleted_images += 1
    else:
        print(f"❌ Image not found: {image_path_jpg}")

    # Delete label file if it exists
    if os.path.exists(label_path):
        os.remove(label_path)
        print(f"🗑️ Deleted label: {label_path}")
        deleted_labels += 1
    else:
        print(f"❌ Label not found: {label_path}")

print(f"\n✅ Done. Deleted {deleted_images} images and {deleted_labels} labels.")
'''

import os

# List of file paths to delete
files_to_delete = [
    "12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-10_jpg.rf.04822e391ecc09bac7f47032501ae204.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-19_jpg.rf.314eb39b4e61cac926f52ae14c977137.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-1_jpg.rf.8da2d4d190c5366f199076b48b25763d.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-2_jpg.rf.56d75ff51de4a41a592e5cec2adf46f3.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-36_jpg.rf.bc3d219f090791cb4ffeec0554ae0801.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-3_jpg.rf.14e06ba0787a1659966fbaf943953436.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-46_jpg.rf.c4500671fdd5d01c5c520b0e29a22fbe.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-48_jpg.rf.1b6b4b9a759758bd17a916f2f3a97c3b.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-4_jpg.rf.8d2ca0bc41d4922053ca7df866fb991c.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-50_jpg.rf.c4e4c9dde8b88473c3496d5989cb1156.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-55_jpg.rf.79ba6b8b8d5b9b9aed33ccfb6a977cdd.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-64_jpg.rf.42084dde3150b1f575657d19cf345f48.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-66_jpg.rf.704f7e6a14994e0fac7423ef99f44b17.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-6_jpg.rf.742903c8db43a011cfb2affedb114e18.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-72_jpg.rf.437e8a6c938d1f88dfbb8f5f10b4731b.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-75_jpg.rf.ece77cb7fc97c8a87b1e5d9062e418d1.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-78_jpg.rf.ba7b00fc4a9714207b46a274dc741ed4.txt"
"12-Kaavan-Male-Elephant-Sleeping-In-The-Jungle-To-Celebrate-World-Elephant-Day-ElephantNews-frame-9_jpg.rf.2d88d111101807f34a86c87eaae34284.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-10_jpg.rf.a84f681ce5f574f8a219fb615688b68f.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-16_jpg.rf.fb9facfeb14642638ca3215b63d1f971.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-17_jpg.rf.47ca21500b5fc7c932e6d85258579b7c.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-21_jpg.rf.cf3584c47df311e28e8445ccc4fa5b9d.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-22_jpg.rf.8d5861d1fe0646c054f48ea47bb891d7.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-23_jpg.rf.b0117951e591e5e2dedb81b19e29a303.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-27_jpg.rf.c26ff5e61d9d78bb053994ddc9d3ccb7.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-29_jpg.rf.7d736a8bfb9bc94bc47261104d33aa0e.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-30_jpg.rf.3d0a5365ebf170e0566581ee4a36819c.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-31_jpg.rf.41f0a2f90c1d8633674931588d3be950.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-33_jpg.rf.5c706aa0e908c887f2938e2e14163d88.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-35_jpg.rf.f16b54a022a24c5ec887ee1faa20cdf1.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-38_jpg.rf.49163f1c085b698af6b567df50c7bc2b.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-3_jpg.rf.501ae387012d737b50a78cc6e221ec94.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-41_jpg.rf.5031124e1ddcada03904d4db295c86b2.txt"
"14-Elephant-Spraying-Water-and-Splashing-Mud-_-Latest-Wildlife-Sightings-_-Kruger-National-Park-frame-5_jpg.rf.7c6aee66fa61543e66eaed897e64e988.txt"
 "20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-10_jpg.rf.46f235297413ce8aa9a4f0b17db9ee13.txt "
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-11_jpg.rf.0e1473e775fc176a438cbbd76d0878a5.txt "
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-12_jpg.rf.259c8cc1cae5c798314c1d03bdb1a95a.txt"
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-15_jpg.rf.5980d44c809fcf778191198e704336d2.txt "
 "20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-18_jpg.rf.ef5ffd6a2c0a5fac2c2ead83d88cfcc2.txt "
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-19_jpg.rf.f57a20452934e371bf3d4e1679d63279.txt" 
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-1_jpg.rf.3223e96ac10081148b056cd5b7d32f1f.txt "
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-23_jpg.rf.336acb4f31c4fa212ae57932844655d9.txt" 
 "20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-2_jpg.rf.bdebbeefa0feb545681cbc1bb3c5d380.txt "
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-30_jpg.rf.c8f8ee4e6ed7d535f50a318a8f76a085.txt "
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-34_jpg.rf.23d7d3b60bd0bd6a6ca54e8bb3c27547.txt "
 "20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-44_jpg.rf.1b226e37ebc784264e544d9ee952e9d7.txt" 
"20-Double-Trouble-Baby-Elephants-Pyi-Mai-And-Chaba-Enjoying-In-The-Hole-ElephantNews-frame-9_jpg.rf.d0f2ab352391375d0a4593dde83f80a1.txt "
 "23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-13_jpg.rf.52dfa99f82e0691209f1132f9fa01a58.txt "
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-15_jpg.rf.3b3e75fd78bc677f14cf1d195d64cc96.txt "
 "23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-17_jpg.rf.2d24f15142c9ea1095273184a6ab5fd2.txt "
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-20_jpg.rf.6f1963f4c1f27d78f3c6d7a88c9f2f75.txt "
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-23_jpg.rf.b173ac6cbedb7c50346740b312bf4b24.txt "
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-26_jpg.rf.dfd51aaaba99c955ec64978d7e1a88bc.txt "
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-28_jpg.rf.2442f0ab44b1dad46cb58b5c3ad24e2a.txt" 
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-2_jpg.rf.c656af16de3557304f4047890155ed5f.txt "
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-31_jpg.rf.37777e448b6ced5d2594694856f69983.txt "
 "23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-38_jpg.rf.c8cd15868fb50c8e634b863bb522b423.txt "
 "23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-3_jpg.rf.30613ab58828b846af6d5457c80ad90c.txt"
 "23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-41_jpg.rf.cec17d1f9e1f80633ac31de2c94aab74.txt"
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-43_jpg.rf.32502c4789279b1825100fa159813dad.txt "
 "23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-4_jpg.rf.0804b01d2e85d8215c63904619c9e47a.txt"
"23-Baby-Elephant-LekLek-And-Her-Mother-Run-Excitingly-To-Enjoy-In-The-River-ElephantNews-frame-6_jpg.rf.09b03a2b9d7ccd4534dede0031c06204.txt "
 "64-elephant-on-musth-aggressive-behaviour-due-to-over-secretion-of-testosterone-please-subscribe-frame-3_jpg.rf.188956bdd32164c9ec28e7407f09082d.txt "
" 80-fight-between-elephant-or-rhinoceros-elephant-Y-VS-rhinoceros-__-animal-life-animallife-1-frame-0_jpg.rf.a956de8af2cc76c020130c0aca5795bc.txt "
"80-fight-between-elephant-or-rhinoceros-elephant-Y-VS-rhinoceros-__-animal-life-animallife-1-frame-3_jpg.rf.7460afb7b4abc63e65e95a93ae16a0d1.txt "
 "80-fight-between-elephant-or-rhinoceros-elephant-Y-VS-rhinoceros-__-animal-life-animallife-1-frame-5_jpg.rf.7485a0c404b476c75bd0198a079bb19e.txt "
 "93-Big-Elephant-_-Biggar-Elephant-_-Biggest-Tusker-_-Big-Wild-Elephant-_-Biggest-Elephant-in-the-world-frame-3_jpg.rf.8a7e6e4c97943f4eb22bf6d67822f577.txt "
 "93-Big-Elephant-_-Biggar-Elephant-_-Biggest-Tusker-_-Big-Wild-Elephant-_-Biggest-Elephant-in-the-world-frame-4_jpg.rf.44aa9e7f2e3a78c94141978903b4115a.txt"
 "93-Big-Elephant-_-Biggar-Elephant-_-Biggest-Tusker-_-Big-Wild-Elephant-_-Biggest-Elephant-in-the-world-frame-7_jpg.rf.ef0f80a19f9577424e27228256611327.txt "
 "MhoJae-begins-to-relax-in-SookSai-s-presence-and-they-care-for-Sa-Ngae-together-a-i-frame-2_jpg.rf.cf51b95ff3302c0e6393e35803ceba5a.txt "
 "MhoJae-begins-to-relax-in-SookSai-s-presence-and-they-care-for-Sa-Ngae-together-a-i-frame-6_jpg.rf.4ea6b5c629502cc6f8551e5e1449c7b9.txt "
 "MhoJae-begins-to-relax-in-SookSai-s-presence-and-they-care-for-Sa-Ngae-together-a-i-frame-8_jpg.rf.cf017f45e06b2c9f399f7e0434fbb4b6.txt "
]

import os

for file_path in os.path.exists(label_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"🗑️ Deleted: {file_path}")
    else:
        print(f"❌ File not found: {file_path}")
