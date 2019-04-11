import numpy as np
import cv2
import pytesseract
from PIL import Image
from difflib import get_close_matches
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

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


ops = ['mozzie', 'gridlock', 'nomad', 'kaid', 'clash', 'maverick', 'maestro', 'alibi',
     'lion', 'finka', 'vigil', 'dokkaebi', 'zofia', 'ela', 'ying', 'lesion', 'mira',
     'jackal', 'hibana', 'echo', 'caveira', 'capitao', 'blackbeard', 'valkyrie', 'buck',
      'frost', 'mute', 'sledge', 'smoke', 'thatcher', 'ash', 'castle', 'pulse', 'thermite',
      'montagne', 'twitch', 'doc', 'rook', 'jager', 'bandit', 'blitz', 'iq', 'fuze', 'glaz', 'tachanka', 'kapkan']

#read the image
image = cv2.imread("image.png")
#get image properties
h, w, c = image.shape

output = []
for i in range(5):
# cut image on each attacker name
  atk = image[round(h*0.425):round(h*0.50), round(w*0.09)+(i*round(w*0.182)):round(w*0.23)+(i*round(w*0.18))]
  # get attacker name
  textatk = text(atk)
  try:
      # get close matches from attackers list and apends to list
      output.append(get_close_matches(textatk.lower(), ops, n=1, cutoff = 0.6)[0])
  except:
      pass

print(output)
