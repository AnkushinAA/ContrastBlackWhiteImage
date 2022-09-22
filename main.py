from PIL import Image
'''def transform(pixel, minIn, maxIn):
    minOut = 0
    maxOut=255
    iO = (pixel - minIn) * (((maxOut - minOut) / (maxIn - minIn)) + minOut)
    return int(iO)'''

def contrastBlackWhiteImage (image):
    result = list()
    for i in range(image.size[0]-1):
        for j in range(image.size[1]-1):
            pixel = image.getpixel((i, j))
            result.append(pixel)
    mi = min(result)
    ma = max(result)
    for i in range(image.size[0]-1):
        for j in range(image.size[1]-1):
            p = image.getpixel((i,j))
            pix = int((p - mi) * (255 / (ma - mi)))
            image.putpixel((i, j), pix)
    print('color min', mi, 'color max',ma)
    return image

imageFileName1 = 'lunar_images/lunar01_raw.jpg'
imageFileName2 = 'lunar_images/lunar02_raw.jpg'
imageFileName3 = 'lunar_images/lunar03_raw.jpg'
original1 = Image.open(imageFileName1)
original2 = Image.open(imageFileName2)
original3 = Image.open(imageFileName3)
newImage1 = contrastBlackWhiteImage(original1)
newImage1.show()
newImage2 = contrastBlackWhiteImage(original2)
newImage2.show()
newImage3 = contrastBlackWhiteImage(original3)
newImage3.show()


