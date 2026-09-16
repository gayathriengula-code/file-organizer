
import os
import shutil

# Find the Downloads folder automatically
home = os.path.expanduser("~")
folder = os.path.join(home, "Downloads")

# Check if Downloads folder exists
if not os.path.exists(folder):
    print("Downloads folder was not found.")
    print("Please check your Downloads folder location.")
    exit()

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Others": []
}

# Check every file in the Downloads folder
for file in os.listdir(folder):

    file_path = os.path.join(folder, file)

    # Ignore folders
    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()
        moved = False

        # Find the correct category
        for category, extensions in categories.items():

            if extension in extensions:

                # Create category folder
                category_folder = os.path.join(folder, category)
                os.makedirs(category_folder, exist_ok=True)

                # Move file
                shutil.move(
                    file_path,
                    os.path.join(category_folder, file)
                )

                print(file, "moved to", category)
                moved = True
                break

        # Move unknown file types to Others
        if not moved:

            other_folder = os.path.join(folder, "Others")
            os.makedirs(other_folder, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(other_folder, file)
            )

            print(file, "moved to Others")

print("File organization completed!")