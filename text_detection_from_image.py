import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\hp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe' \
                                        r''#\Tesseract-OCR\tesseract.exe

img = cv2.imread("Resources/pytesseract_test.png")
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


cv2.imshow("out",img)

text = pytesseract.image_to_string(rgb)
print(text)

# cv2.imshow("out",rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()
