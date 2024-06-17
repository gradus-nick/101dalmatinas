from pyzbar import pyzbar
import cv2
import tempfile
import numpy as np
import os

def decode(image):
    # расшифровываем все штрихкоды которые нашли
    mBarcode = []
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        
        type = obj.type
        data = obj.data.decode('UTF-8')
        orientation = obj.orientation

        result = {'type':type, 'data':data, 'orientation':orientation}
        mBarcode.append(result)

    return mBarcode

def findbarcodepng(file):
    tempdir = tempfile.gettempdir()

    file_location = tempdir + '/' + file.filename

    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    # загружаем картинку в opencv
    img = cv2.imread(file_location)
    
    # расшифровываем найденные штрихкоды
    mBarcode = decode(img)
    # если ничего не нашли возможно файл шумный пробуем выкрутить яркость сгладить резкость и распознать снова
    if len(mBarcode)==0:
        morph_kernel = np.ones((3, 3))
        
        erode_img = cv2.erode(img, kernel= morph_kernel, iterations=1)
        gaus_img = cv2.medianBlur(erode_img,3)
        
        mBarcode = decode(gaus_img)
    
    os.remove(file_location)
    return mBarcode 
   
