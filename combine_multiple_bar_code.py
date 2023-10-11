from PIL import Image
import qrcode
from pyzbar.pyzbar import decode, ZBarSymbol
def decoder(image):
    list_of_all_barcode=[]
    barcode = decode(image)
    for x in barcode:
        barcodeData = x.data.decode("utf-8")
        list_of_all_barcode.append(str(barcodeData))
    return list_of_all_barcode
image = Image.open("./QR_CODE/merge_s.png")
qrcodes_list=list(decoder(image))[::-1]
qr = qrcode.QRCode(version = 1,
				box_size = 10,
				border = 5)
for x in qrcodes_list:
    qr.add_data(x+',')
img = qr.make_image(fill_color = 'black',
					back_color = 'white')
img=img.resize((100,100))
img.save('./QR_CODE/final_scanned_data.png')
