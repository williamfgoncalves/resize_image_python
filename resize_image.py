import warnings                                                                                                 
warnings.filterwarnings("ignore")
import cv2
import os

def main():

	IN_PATH = location("\in_img")
	OUT_PATH = location("\out_img")

	for image_name in os.listdir(IN_PATH):
		im = cv2.imread(os.path.join(IN_PATH, image_name))
		print(im.shape)
		im_resize = cv2.resize(im, (1024, resize(1024, im.shape[0], im.shape[1])))
		cv2.imwrite(os.path.join(OUT_PATH, image_name), im_resize)
	

def location(path):
	dirname = os.path.abspath(os.getcwd())
	return dirname + path

def resize(a, b, c):
	return (a * b) / c 

if __name__ == "__main__":
	main()

# im_shape[0]
# im_shape[0]
# im_shape[0]
	
#fixar largura em 1024 e altura varia de acordo com a nova largura 