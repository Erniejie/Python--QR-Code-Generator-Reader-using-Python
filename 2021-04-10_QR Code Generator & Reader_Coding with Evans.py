"QR Code Generator & Reader using Python "
"Coding with evan_June 21,2020"
#pip install pyqrcode
#pip install pypng
#pip install pillow
#pip install pyzbar
#------------------------------
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Coding With Yijie")
qr.png("ErniesCode.png",scale=8)

#Decoding a QRCODE

d = decode(Image.open("ErniesCode.png"))
#print(d)
print(d[0].data.decode("ascii"))
