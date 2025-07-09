'''This module handles the text recognition model.

 Current: Using EasyOCR (lightweight & simple).
 Future Plans:
    - Replace with a custom deep learning model (e.g., CRNN, CNN+RNN+CTC).
    - Fine-tuned on handwritten datasets like IAM or CVL.
    - Must accept raw CV2 images (not PIL).
    - Should generalize to messy handwriting and various backgrounds.
""" '''