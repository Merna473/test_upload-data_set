import os
import kagglehub

dataset_path = kagglehub.dataset_download("mohamedgharzouli/digital-drug-music")

for folder_name in ["DD", "NDD"]:
    root_dir = os.path.join(dataset_path, folder_name)
    subfolders = []
    audio_files = []
    extensions = set()

    for current_root, dirs, files in os.walk(root_dir):
        for d in dirs:
            subfolders.append(os.path.relpath(os.path.join(current_root, d), root_dir))
        for f in files:
            full_path = os.path.join(current_root, f)
            audio_files.append(full_path)
            extensions.add(os.path.splitext(f)[1].lower())

    print(f"=== {folder_name} ===")
    print("Subfolders count:", len(subfolders), "| Sample:", subfolders[:5])
    print("Total files inside:", len(audio_files), "| Extensions:", extensions)
    print("Sample files:", [os.path.basename(p) for p in audio_files[:3]])