import os
import kagglehub

DATASET_HANDLE = "mohamedgharzouli/digital-drug-music"
dataset_path = kagglehub.dataset_download(DATASET_HANDLE)

for folder_name in ["DD", "NDD"]:
    folder_path = os.path.join(dataset_path, folder_name)
    exists = os.path.exists(folder_path)
    count = len(os.listdir(folder_path)) if exists else 0
    print(f"{folder_name} -> exists: {exists}, items: {count}")