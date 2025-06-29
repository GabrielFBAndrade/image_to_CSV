
import easyocr
reader = easyocr.Reader(['en'])
results = reader.readtext('/Users/gabrielfelix/Desktop/Python Projects/OCR_Project/sample.png')

for detection in results:
    print(detection[1])


