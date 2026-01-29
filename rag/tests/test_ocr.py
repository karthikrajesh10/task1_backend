from PIL import Image
import pytesseract

# 👇 ADD THIS LINE (VERY IMPORTANT)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open("tts_stt_backend/rag/documents/images/testocr.png")
text = pytesseract.image_to_string(img)

print("OCR OUTPUT:")
print(text)
