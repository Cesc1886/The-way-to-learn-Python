from PIL import Image
import numpy as np

a = np.array(Image.open("C:/Users/Erdi Chen/Desktop/Python/Datenanalyse/SH.jpg").convert('L'))

##d = 255* (a/255) **2   # 黑白图像

depth = 10.             # 预设为10，取值0-100
grad = np.gradient(a)
grad_x,grad_y = grad
grad_x = grad_x * depth / 100.
grad_y = grad_y * depth / 100.

vec_el = np.pi / 2.2  # 俯仰角
vec_az = np.pi / 4.   # 方位角
dx = np.cos(vec_el) * np.cos(vec_az)     # 单位光线在地面的投影长度
dy = np.cos(vec_el) * np.sin(vec_az)
dz = np.sin(vec_el)         # dx,dy,dz 是光源对x,y,z三个方向的物体明暗的影响程度

A = np.sqrt(grad_x **2 + grad_y **2 + 1.)    # 归一化
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A

b = 255* (dx*uni_x + dy* uni_y + dz * uni_z)     # 梯度与光源相互作用，将梯度转化为灰度

b = b.clip(0,255)

im = Image.fromarray(b.astype('uint8'))
im.save("C:/Users/Erdi Chen/Desktop/Python/Datenanalyse/Gray_SH.jpg")