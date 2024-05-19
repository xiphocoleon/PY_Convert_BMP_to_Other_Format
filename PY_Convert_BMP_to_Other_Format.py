from PIL import Image
import glob
import os

#Dimensions of resized images
dimX = 300
dimY = 300

#Path to BMP images:
root_dir = 'C:\\Users\\thoma\\Pictures\\Geodis\\3473SRP-lane 2 fails'
path_to_bmps = root_dir + '\\*.BMP'

#Path to converted images:
path_to_reformatted_images = root_dir + '\\png'
os.mkdir(path_to_reformatted_images)


def convert_BMP_to_PNG():
    cnt = 0
    for img in glob.glob(path_to_bmps):
        Image.open(img).resize((dimX,dimY)).save(os.path.join(path_to_reformatted_images, str(cnt) + '.png'))
        cnt += 1

def copy_images_in_PNG_folder_to_all_images_folder():
    #To be developed later
    dummy = 0
    
