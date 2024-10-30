from PIL import Image #pip install pillow

import os

downloads_Folder = "C:/Users/WobistduTech/Downloads/"
Pictures_Folder = "C:/Users/WobistduTech/Pictures/"

if __name__ == "__main__":
    for filename in os.listdir(downloads_Folder):
        name, extension = os.path.splitext(downloads_Folder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloads_Folder + filename)
            picture.save(downloads_Folder + "compressed_" + filename, optimize=True, quality=60)
            os.remove(downloads_Folder + filename)
            print(name + ": " + extension)

            if extension in [".mp3"]:
                music_Folder = "C:/Users/WobistduTech/Music"
                os.rename(downloads_Folder + filename, music_Folder + filename)