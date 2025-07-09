#import packages

import cv2
from ocr_pipeline import textExtraction
from translator import translationHindi, translationUrdu
import numpy as np
from printLanguages import non_latin_text
import tkinter as tk
from tkinter import simpledialog

urdu_path = r"assets\NotoNastaliqUrdu-Regular.ttf"
hindi_path =r"assets\NotoSansDevanagari-Regular.ttf"

def askLang():
    # Prepare a pop up to ask user which language to translate in
    root = tk.Tk()
    root.withdraw()
    ask = simpledialog.askstring("Choose Language", "H for hindi or U for Urdu")
    ask = ask.strip().upper()
    root.destroy()
    return ask

chosenLang = askLang()
def run(image, selectedLang):
    # read the text in english 
    english, rectangles = textExtraction(image)

    # Convert English to Hindi and Urdu text
    hindiText = [translationHindi(english[i]) for i in range(len(english))]
    urduText = [translationUrdu(english[i]) for i in range(len(english))]

    final_text = " "

    if selectedLang == "H":
        path = hindi_path
        final_text = hindiText
    elif selectedLang == "U":
        path = urdu_path
        final_text = urduText
    else:
        raise ValueError("Not a valid language, please enter the language specified")

    # Blurr the english text
    for i, rect in enumerate(rectangles):
        pts1 = rect[0]
        pts2 = rect[1]
        text_region = image[pts1[1]: pts2[1], pts1[0]: pts2[0]]
        text_region = cv2.GaussianBlur(text_region, (35, 35), 15)
        image[pts1[1]: pts2[1], pts1[0]: pts2[0]] = text_region

        # display the text in user's selected language
        image = non_latin_text(image, final_text[i], pts1, path, 20, (0, 0, 0))

    return image

import tkinter as tk
from tkinter import messagebox

def ask_mode():
    def on_image():
        user_choice.set("image")
        window.destroy()

    def on_webcam():
        user_choice.set("webcam")
        window.destroy()

    window = tk.Tk()
    window.title("Choose Input Mode")
    window.geometry("300x150")
    window.eval('tk::PlaceWindow . center')

    user_choice = tk.StringVar()

    label = tk.Label(window, text="Select input type:", font=("Arial", 12))
    label.pack(pady=10)

    image_btn = tk.Button(window, text="Upload Image", command=on_image, width=20, bg="#4CAF50", fg="white")
    image_btn.pack(pady=5)

    webcam_btn = tk.Button(window, text="Use Webcam", command=on_webcam, width=20, bg="#2196F3", fg="white")
    webcam_btn.pack(pady=5)

    window.mainloop()
    return user_choice.get()

mode = ask_mode()

if mode == "image":
    from tkinter import filedialog
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    img = cv2.imread(filepath)
    img_translated = run(img, chosenLang)

    cv2.imshow("Translation",img_translated)
    cv2.waitKey(0)

elif mode == "webcam":
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    while True:
        success, img = cap.read()
        img_translated = run(img, chosenLang)

        cv2.imshow("Live Translation", img_translated)
        if(cv2.waitKey(1) and 0xff == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()

else:
    print("No option selected.")
