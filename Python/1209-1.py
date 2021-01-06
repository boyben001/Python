import PIL
from PIL import Image

image = Image.open(
    'C:/Users/BEN_CHEN/Desktop/vscode/Python/Ch06/sample_image/flower.jpg')
image.show()
r, g, b = image.split()
convert_image = Image.merge("RGB", (b, g, r))
convert_image.show()
convert_image.save(
    'C:/Users/BEN_CHEN/Desktop/vscode/Python/Ch06/sample_image/rgb_to_bgr.jpg')
black_and_white = image.convert('1')  # 參數1代表1 bit單位元的黑白圖片
black_and_white.show()
black_and_white.save(
    'C:/Users/BEN_CHEN/Desktop/vscode/Python/Ch06/sample_image/black_white.jpg')
gray_image = image.convert("L")  # 轉成灰階
gray_image.show()
gray_image.save(
    'C:/Users/BEN_CHEN/Desktop/vscode/Python/Ch06/sample_image/gray color.jpg')
image.transpose(Image.ROTATE_90).show()
image.transpose(Image.ROTATE_90).save('rotate_90.jpg')
