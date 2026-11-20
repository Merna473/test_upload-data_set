import os
import kagglehub

path = kagglehub.dataset_download("mohamedgharzouli/digital-drug-music")
print("المسار:", path)
print("موجود فعلاً؟", os.path.exists(path))

total_files = 0
total_size = 0

for root, dirs, files in os.walk(path):
    total_files += len(files)
    for f in files:
        total_size += os.path.getsize(os.path.join(root, f))

print("المحتويات الرئيسية:", os.listdir(path))
print("إجمالي عدد الملفات:", total_files)
print(f"إجمالي الحجم: {total_size / (1024**3):.2f} GB")