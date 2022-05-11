# Rename all images in training data (old names were too complex)
import os

def main():
    folder_images = "/Users/fletcherpearmaine/Desktop/Handgun_images/images" # images directory
    folder_labels = "/Users/fletcherpearmaine/Desktop/Handgun_images/labels" # labels directory

    # images
    for count, filename in enumerate(os.listdir(folder_images)): # iterate through every image file
        destination = f"Image {str(count)}.jpg"
        source =f"{folder_images}/{filename}" # foldername/filename
        destination =f"{folder_images}/{destination}"
        os.rename(source, destination)# rename() renames each of the files

    # labels
    for count, filename in enumerate(os.listdir(folder)): # iterate through every label file
        destination = f"Image {str(count)}.jpg"
        source =f"{folder}/{filename}"
        destination =f"{folder}/{destination}"
        os.rename(source, destination)

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
