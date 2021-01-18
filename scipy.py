from scipy.misc import imread, imsave, imresize

img = imread('C:/Users/Lenovo/Desktop/Testing/Dppic.jpg')
print(img.dtype, img.shape)

img_tint = img * [1, 0.45, 0.3]

imsave('C:/Users/Lenovo/Desktop/Testing/Dppic_tinted.jpg', img_tint)

img_tint_resize = imresize(img_tint, (300,300))

imsave('C:/Users/Lenovo/Desktop/Testing/Dppic_resized.jpg', img_tint_resize)
