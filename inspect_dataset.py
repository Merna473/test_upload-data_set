import os
import numpy as np
import kagglehub

# 1. Get dataset path from local cache
dataset_path = kagglehub.dataset_download("mohamedgharzouli/digital-drug-music")
print("Dataset Path:", dataset_path)
print("-" * 50)

# 2. Check DD and NDD folders
for folder_name in ["DD", "NDD"]:
    folder_path = os.path.join(dataset_path, folder_name)
    if os.path.exists(folder_path):
        files = [
            f for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ]
        extensions = set(os.path.splitext(f)[1].lower() for f in files)
        print(f"Folder '{folder_name}': {len(files)} files | Extensions: {extensions}")
        print(f"  Sample files: {files[:3]}")
    else:
        print(f"Folder '{folder_name}' not found!")

print("-" * 50)

# 3. Inspect .npy files (features and labels)
features_path = os.path.join(dataset_path, "combined_features_list.npy")
labels_path = os.path.join(dataset_path, "labels.npy")

if os.path.exists(features_path):
    features = np.load(features_path, allow_pickle=True)
    print("combined_features_list.npy -> shape:", features.shape, "| dtype:", features.dtype)

if os.path.exists(labels_path):
    labels = np.load(labels_path, allow_pickle=True)
    unique_labels, counts = np.unique(labels, return_counts=True)
    print("labels.npy -> shape:", labels.shape, "| dtype:", labels.dtype)
    print("Label distribution:", dict(zip(unique_labels, counts)))