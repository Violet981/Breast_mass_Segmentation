import os
import cv2
import numpy as np
import re

textFile = 'Dice.txt'
def otsu(root_dir):
	for item in os.listdir(root_dir):
		item_path = os.path.join(root_dir, item)
		img = cv2.imread(item_path, cv2.IMREAD_GRAYSCALE)
		ret, th = cv2.threshold(img,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
		cv2.imwrite(os.path.join(root_dir, item), th)

def getDice(result_dir, gt_dir):
	Total_dice = 0
	num = 0
	file_write_obj = open(textFile, 'w')
	for result_item in os.listdir(result_dir):
		result_path = os.path.join(result_dir, result_item)
		img_number = re.findall("\d+", result_item)[0]
		gt_path = os.path.join(gt_dir, 'valid_mask_' + str(img_number) + '.png')

		print(gt_path)
		file_write_obj.write(str(gt_path) + "\n")

		result = cv2.imread(result_path, cv2.IMREAD_GRAYSCALE)
		gt = cv2.imread(gt_path, cv2.IMREAD_GRAYSCALE)

		row, col = gt.shape[0], gt.shape[1]
		s = []
		for r in range(row):
			for c in range(col):
				if result[r][c] == gt[r][c]:
					s.append(result[r][c])
		m1 = np.linalg.norm(s)
		m2 = np.linalg.norm(result.flatten()) + np.linalg.norm(gt.flatten())
		dice = 2 * m1 / m2
		Total_dice += dice
		num += 1

		print(dice)
		file_write_obj.write(str(dice) + "\n")
		print("---------------")
		file_write_obj.write("----------------\n")
	Avg_dice = Total_dice / num
	print("Avg :" + str(Avg_dice))
	file_write_obj.write("Avg: " + str(Avg_dice) + "\n")
	file_write_obj.close()

#otsu('result')
getDice('result', 'gt')