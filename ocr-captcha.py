#import matplotlib.pyplot as plt
import urllib
from urllib.request import urlopen
from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url='https://www.gsctx.org/en/our-council/web-to-case.html'

response = urlopen(url)
html = response.read().decode('utf-8')

url_captcha = re.findall(r'<img id=\"cq_captchaimg\" src=\"/content/gsctx/en/our-council/web-to-case/_jcr_content/content/middle/par/captcha\.captcha\.png\?id=123\" alt=\"\"></div>', html)[0]
id_captcha=re.findall(r'[0-9]+',str(url_captcha))
#print(id_captcha[0])

url_captcha = 'https://www.gsctx.org/en/our-council/web-to-case/jcr:content/content/middle/par/captcha.captcha.png?id='+str(id_captcha[0])
image = Image.open(urllib.request.urlopen(url_captcha))


captcha=pytesseract.image_to_string(image)
print("Request\n",url)
print("Response\n Captcha CODE: ",captcha)

#plt.imshow(image)
#plt.show()