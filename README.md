# OCR and Translation of Handwritten Text

This project is a computer vision and natural language processing (NLP) pipeline that detects **handwritten English text** from an image or webcam stream, translates it into **Hindi or Urdu**, and **overlays the translated text back onto the original image**. It supports real-time translation using a webcam and static image uploads.


## 📌 Features

* Detects **handwritten English text** using EasyOCR
* Translates detected text to **Hindi or Urdu** using Hugging Face Transformers
* Applies **Gaussian blur** to original English text regions for privacy and aesthetics
* Displays **translated text** using appropriate Unicode fonts
* Supports input from **image upload** or **live webcam feed**
* Built with **OpenCV, EasyOCR, Transformers, and Tkinter**


## 🧠 Motivation

Most OCR systems are tuned for printed text and lack robustness in translating real-world, handwritten data, especially in a multilingual context. This project was created to:

* Bridge the gap between OCR and live translation
* Handle multilingual rendering in a single app
* Serve as a base for more advanced document translators or assistive reading tools


## 🛠️ Tech Stack

| Tool         | Purpose                                |
| ------------ | -------------------------------------- |
| Python 3.12  | Programming language                   |
| EasyOCR      | OCR for handwritten English text       |
| Hugging Face | Language translation models            |
| OpenCV       | Image processing and visualization     |
| Tkinter      | User prompts (input mode and language) |
| Noto Fonts   | Hindi and Urdu font rendering          |


## 🔄 Pipeline Overview

1. **Input Selection**: Prompt the user to choose between image upload or webcam.
2. **Language Choice**: Ask user to select translation language (Hindi or Urdu).
3. **Text Detection**: Use EasyOCR to extract English text and bounding boxes.
4. **Text Translation**: Translate text via Hugging Face pipelines:

   * `Helsinki-NLP/opus-mt-en-hi` (Hindi)
   * `Helsinki-NLP/opus-mt-en-ur` (Urdu)
5. **Text Replacement**:

   * Blur the original text region
   * Overlay the translated text using appropriate font

---

## 📁 Project Structure

```
Translator-ML/
├── assets/                      # Fonts for Hindi and Urdu
│   ├── NotoSansDevanagari-Regular.ttf
│   └── NotoNastaliqUrdu-Regular.ttf
├── src/
│   ├── main.py                  # Main entry point with GUI logic
│   ├── ocr_pipeline.py         # Text detection logic (EasyOCR)
│   ├── translator.py           # Hugging Face translation functions
│   ├── printLanguages.py       # Utility to print translated text using custom fonts
│   └── model.py                # Placeholder for future fine-tuned model
└── requirements.txt            # Python dependencies
```

---

## ▶️ How to Run

1. **Clone the repository**

```bash
https://github.com/satvik-18/Translator-ML
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
python src/main.py
```

4. **Follow prompts**:

   * Choose between webcam or image upload
   * Choose language: `H` for Hindi, `U` for Urdu

5. Press `q` to exit webcam mode

---

## ⚠️ Known Issues

* EasyOCR is not perfect for messy handwriting
* Real-time webcam translation might feel slow on CPU-only systems
* Fonts must support full Unicode for multilingual rendering

---

## 💡 Future Improvements

* Fine-tune OCR model on handwriting datasets (IAM, CVL)
* Add more language options
* Use voice-to-text and text-to-speech (TTS) for accessibility
* Export results as PDFs or images

---

## 🙏 Acknowledgments

* [EasyOCR](https://github.com/JaidedAI/EasyOCR)
* [Hugging Face Transformers](https://huggingface.co/models)
* [Noto Fonts](https://www.google.com/get/noto/)
* [OpenCV](https://opencv.org/)



