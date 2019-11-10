from PIL import Image
import numpy as np

a = np.array(Image.open("C:/Users/Erdi Chen/Desktop/Python/Datenanalyse/SH.jpg").convert('L'))

b = 255* (a/255) **2   ## 黑白图像
im = Image.fromarray(b.astype('uint8'))
im.save("C:/Users/Erdi Chen/Desktop/Python/Datenanalyse/Gray01_SH.jpg")