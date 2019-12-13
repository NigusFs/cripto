#Python 3.6.7
#reference https://pypi.org/project/pytesseract/
#by NFS
import urllib
from urllib.request import urlopen
from PIL import Image
import pytesseract
import re
import sys

#pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe' #it is useful with windows

url_burp=str(sys.argv[1]) #url from burp suite

image = Image.open(urllib.request.urlopen(url_burp))
captcha=pytesseract.image_to_string(image) #ocr

print("Request")
print(url_burp)
print("Response\nCaptcha CODE: ",captcha)

#plt.imshow(image)
#plt.show()
