# packages

import cv2
import easyocr

#Detect and Reading Text

reader = easyocr.Reader(['en'])
def textExtraction(image):

    if(image is  None):
        raise FileNotFoundError("Cant Find the image")
    
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    results = reader.readtext(grey)
    detected_text = []

#UI edits and exporting text for other functions
    rectangles = ()
    for(bbox, text, score) in results:
        if score>0.5:
            detected_text.append(text)
            pts1 = tuple(map(int, bbox[0]))
            pts2 = tuple(map(int, bbox[2]))

            rect = (pts1, pts2)
            rectangles += (rect,)
    
    return detected_text, rectangles







