import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import pydicom
import os

pathImages = 'CAMINHO/DAS/IMAGENS'

roiLocation = pd.read_csv('roiLocation.csv', index_col=0)

roiLocation = roiLocation.groupby(by='imageName')

for name, group in roiLocation:
    ### Abrir a imagem em Dicom
    img_name = [data_name for data_name in os.listdir(pathImages) if str(name) in data_name][0]

    dicom_file = pydicom.dcmread(os.path.join(pathImages, img_name))
    org_array = dicom_file.pixel_array

    #### Normalizar a imagem original
    img_array =  org_array/4095

    ### Plotar imagem original (matplotlib)
    plt.imshow(np.int16(img_array*4095), cmap='gray', vmin=0, vmax=4095)
    plt.axis(False)
    plt.show()

    for index, row in group.iterrows():
        ### Recortar imagem
        roi_array = img_array[row['x0']:row['x1'], row['y0']:row['y1']]

        ### Plotar ROI
        plt.imshow(np.int16(roi_array*4095), cmap='gray', vmin=0, vmax=4095)
        plt.axis(False)
        plt.show()

        print('END: 100x100 region')

    print('END: Image')

print('END: Code')