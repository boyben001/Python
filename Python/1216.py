# https://kknews.cc/zh-tw/code/4jv82zx.html
import PIL
from PIL import Image
from PIL import ImageFilter

image = Image.open('C:/Users/BEN_CHEN/Desktop/vscode/the big bang.jpg')
image.show()  # 原檔顯示

left = 200
up = 200
right = 200
down = 200
#(x, y, x + width, y + height)
crop_image = image.crop((left, up, left+right, up+down))
crop_image.show()
crop_image.save('C:/Users/BEN_CHEN/Desktop/vscode/sheldon.jpg')

blur_sheldon = crop_image
for i in range(20):
    blur_sheldon = blur_sheldon.filter(ImageFilter.BLUR)
blur_sheldon.show()
blur_sheldon.save('C:/Users/BEN_CHEN/Desktop/vscode/blur_sheldon.jpg')

EMBOSS_sheldon = crop_image.filter(ImageFilter.EMBOSS)
EMBOSS_sheldon.show()
EMBOSS_sheldon.save('C:/Users/BEN_CHEN/Desktop/vscode/EMBOSS_sheldon.jpg')
