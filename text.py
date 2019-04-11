import numpy as np
import cv2
import pytesseract
from PIL import Image
from difflib import get_close_matches
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract"

def text(img):
    cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    ret, mask = cv2.threshold(img, 155, 255, cv2.THRESH_BINARY_INV)
    img = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    img = cv2.bilateralFilter(img, 9,75,75)

    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    result = pytesseract.image_to_string(Image.fromarray(img))
    return str(result)


ops = ["KingBlazeIV", "Trank", "TIMMAY67", "Gyrogue |", "Massadio", "||| QUickz |||", "Ryasoki", "EdibleHornet",
     "xRazbxrry", "Jonboy507", "xSkreeminSkullx", "CharlieAddo2", "BROZ"]

#read the image
image = cv2.imread("image.jpg")
#get image properties
h, w = 1080, 1920

output = []
for i in range(14):
    # cut image on each name
    j = (i*round(w*0.0211))
    name = image[round(h*0.21)+j:round(h*0.25)+j, round(w*0.18):round(w*0.28)]
    # get name
    nametext = text(name)
    print(nametext)

    # display image while processing (press q to skip to next image)
    # cv2.imshow("image", name)
    # cv2.waitKey(0)

    try:
        # get close matches from attackers list and apends to list
        output.append(get_close_matches(nametext, ops, n=1, cutoff = 0.6)[0])
    except:
        pass

print(output)
