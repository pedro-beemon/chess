# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from chromedriver_py import binary_path as chrome_binary_path

# URL = ''

# driver = webdriver.Chrome(
#     chrome_binary_path,
# )
# driver.get(URL)

# i = 0

# i= 0
# for image in driver.find_elements(By.TAG_NAME,'img'):
#     i += 1
#     if image.size['width']>1:
#         image.screenshot(f'./carro/carro{i}.png')
import cv2
import os

# for file in os.listdir('positivas'):
#     img = cv2.imread("positivas/"+file,cv2.IMREAD_GRAYSCALE)

#     imagem_redimensionada = cv2.resize(img, (100,100))
#     cv2.imwrite("positivas/grey"+file,imagem_redimensionada)

# for file in os.listdir('negativas'):
#     img = cv2.imread("negativas/"+file,cv2.IMREAD_GRAYSCALE)

#     imagem_redimensionada = cv2.resize(img, (100,100))
#     cv2.imwrite("negativas/grey"+file,imagem_redimensionada)

import urllib
import numpy as np
import cv2
import os

for file_type in ['negativas', 'positivas']:
    for img in os.listdir(file_type):
        if file_type == 'negativas':
            line = file_type + '/' + img + '\n'

            with open('bg.txt', 'a') as f:
                f.write(line)

        elif file_type == 'positivas':
            line = file_type + '/' + img + ' 1 0 0 150 150\n'

            with open('info.dat', 'a') as f:
                f.write(line)
