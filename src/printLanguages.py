import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def non_latin_text(cv2_image, text, position, font_path, font_size, color = (0,0,0)):

    PIL_img = Image.fromarray(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(PIL_img)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, font =  font, fill = color)
    
    re_cv2 = np.array(PIL_img)
    re_cv2= cv2.cvtColor(re_cv2, cv2.COLOR_RGB2BGR)
    return re_cv2

