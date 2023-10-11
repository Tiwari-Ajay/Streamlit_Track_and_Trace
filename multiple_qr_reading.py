from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol
import qrcode
def decoder(image):
    list_of_all_barcode=[]
    barcode = decode(image)
    for x in barcode:
        barcodeData = x.data.decode("utf-8")
        list_of_all_barcode.append(str(barcodeData))
    return list_of_all_barcode

image = Image.open("./QR_CODE/QR_s.png")
barcodes_list=list(decoder(image))[::-1]
qr = qrcode.QRCode(version=1,box_size=10,border=5)
for x in barcodes_list[0:3]:
    qr.add_data(x)
    qr.add_data(",")
    print(x)
qr.make(fit=True)
img = qr.make_image(fill_color='black',back_color='white')
img=img.resize((100,100))
file_name = "QR_code_final_temp" + '.png'
img.save(f"./QR_CODE/{file_name}")

image = Image.open("./QR_CODE/QR_code_final_temp.png")
barcodes_list=decode(image)
print(barcodes_list)