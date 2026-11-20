import os
import kagglehub

dataset_path = kagglehub.dataset_download("mohamedgharzouli/digital-drug-music")

print("Dataset path:", dataset_path)
print("Exists:", os.path.exists(dataset_path))
print("Contents:", os.listdir(dataset_path))