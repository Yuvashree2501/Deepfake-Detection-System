import os
import random

# ==============================
# SETTINGS
# ==============================
KEEP_COUNT = 2000   # number of images to keep in each folder

REAL_PATH = "../dataset/real"
FAKE_PATH = "../dataset/fake"


# ==============================
# FUNCTION TO CLEAN FOLDER
# ==============================
def clean_folder(folder_path, keep_count):

    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    # Get only image files
    images = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ]

    total_images = len(images)

    print(f"\n📁 {folder_path}")
    print(f"Before: {total_images} images")

    # If already small, skip
    if total_images <= keep_count:
        print(f"✔ Already less than {keep_count}, no need to clean")
        return

    # Shuffle images randomly
    random.shuffle(images)

    # Split keep & delete
    keep_images = images[:keep_count]
    delete_images = images[keep_count:]

    # Delete extra images
    deleted_count = 0
    for img in delete_images:
        try:
            os.remove(os.path.join(folder_path, img))
            deleted_count += 1
        except Exception as e:
            print(f"⚠ Error deleting {img}: {e}")

    print(f"Deleted: {deleted_count}")
    print(f"After: {keep_count} images")


# ==============================
# RUN CLEANING
# ==============================
if __name__ == "__main__":

    print("🚀 Cleaning Dataset...\n")

    clean_folder(REAL_PATH, KEEP_COUNT)
    clean_folder(FAKE_PATH, KEEP_COUNT)

    print("\n✅ Dataset cleaning completed!")