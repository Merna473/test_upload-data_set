import os
import kagglehub

DATASET_HANDLE = "mohamedgharzouli/digital-drug-music"
dataset_path = kagglehub.dataset_download(DATASET_HANDLE)

file_count = 0
total_bytes = 0

for root, _, files in os.walk(dataset_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        if os.path.exists(file_path):
            file_count += 1
            total_bytes += os.path.getsize(file_path)

total_gb = total_bytes / (1024 ** 3)
print("Dataset path:", dataset_path)
print("Total files:", file_count)
print(f"Total size: {total_gb:.2f} GB")