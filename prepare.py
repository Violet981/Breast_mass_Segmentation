#coding:utf-8
import os
import cv2
import numpy as np
import math

# since the network requires 128 * 128 images, normal images should be flatten and scale
def scaleNflatten(png_path, scale_png_path):
	for img_item in os.listdir(png_path):
		img_path = os.path.join(png_path, img_item)
		img = cv2.imread(img_path)

		ready_to_draw = img
		ready_to_draw = cv2.resize(img[:,:,0],(128, 128), interpolation=cv2.INTER_AREA)
		try:
			cv2.imwrite(os.path.join(scale_png_path, img_item), ready_to_draw)
			print("scaling" + img_path + "---" + str(ready_to_draw.shape))
		except:
			print("sth wrong with scaling ------------------------------" + img_item)

scaleNflatten('tmp_in', 'train_data_in')
scaleNflatten('tmp_out', 'train_data_out')