from PIL import Image
from pyzbar.pyzbar import decode
def decoder(image):
    list_of_all_barcode=[]
    barcode = decode(image)
    for x in barcode:
        barcodeData = x.data.decode("utf-8")
        list_of_all_barcode.append(str(barcodeData))
    return list_of_all_barcode
#image = Image.open("single_image_test.jpg") #reading barcode with image having single barcode
#image = Image.open("multiple_image_test.png") #reading barcodes with image having multiple barcodes
image = Image.open("QR_CODE/temp/QR_code1.png")
barcodes_list=list(decoder(image))[::-1]

print(f"All bar codes are : {barcodes_list}")
