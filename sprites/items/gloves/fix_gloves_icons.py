import os, shutil

# Adjust this path!
base = r"C:\GAMES\crazysport_v30\public\sprites\items\gloves"

count = 0
for folder in os.listdir(base):
    folder_path = os.path.join(base, folder)
    if not os.path.isdir(folder_path):
        continue
    
    icon_path = os.path.join(folder_path, "icon.png")
    icon1_path = os.path.join(folder_path, "icon1.png")
    
    # If icon.png already exists, skip
    if os.path.exists(icon_path):
        continue
    
    # Copy icon1.png -> icon.png
    if os.path.exists(icon1_path):
        shutil.copy2(icon1_path, icon_path)
        count += 1
        print(f"  + {folder}/icon.png (from icon1)")

print(f"\nDone! Created {count} icon.png files")
