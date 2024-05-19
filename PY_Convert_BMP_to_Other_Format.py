from PIL import Image
import glob
import os

#Path to BMP images:
path_to_bmps = 'C:\\Users\\thoma\\Pictures\\Geodis\\2979R21-lane1\\*.BMP'

#Path to converted images:
path_to_reformatted_images = 'C:\\Users\\thoma\\Pictures\\Geodis\\2979R21-lane1\\png'
os.mkdir(path_to_reformatted_images)

cnt = 0
for img in glob.glob(path_to_bmps):
    Image.open(img).resize((300,300)).save(os.path.join(path_to_reformatted_images, str(cnt) + '.png'))
    cnt += 1


