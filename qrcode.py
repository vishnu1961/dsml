import pyqrcode
from pyqrcode import QRCode
s=input("enter the url")
myqr=input("enter your file name")
url=pyqrcode.create(s)
url.svg(myqr+".svg",scale=8)