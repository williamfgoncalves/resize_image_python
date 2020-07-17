import warnings                                                                                                 
warnings.filterwarnings("ignore")
import cv2
import os

def main():

	IN_PATH = "/c/Users/william.goncalves.CWINET/Documents/Pessoal/topicos_avancados_2/in_img"
	OUT_PATH = "/c/Users/william.goncalves.CWINET/Documents/Pessoal/topicos_avancados_2/out_img"

	for image_name in os.listdir(IN_PATH):
		im = cv2.imread(os.path.join(IN_PATH, image_name))
		im_resize = cv2.resize(im, (256,256))
		cv2.imwrite(os.path.join(OUT_PATH, image_name), im_resize)
	
if __name__ == "__main__":
	main()

# im_shape[0]
# im_shape[0]
# im_shape[0]
	
#fixar largura em 1024 e altura varia de acordo com a nova largura 