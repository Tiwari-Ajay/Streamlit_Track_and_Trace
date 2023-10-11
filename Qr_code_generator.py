# Importing library
import qrcode
import pandas as pd
###############
#save data into csv file
brand=pd.Series(["Signature","Signature","RoyalStag"],name='Brnd')
quantity=pd.Series(["750","650","500"], name='Qty')
amount=pd.Series([220,180,150], name='Amt')
combine_data=pd.concat([brand,quantity,amount], axis=1)
combine_data.to_csv('product_data_Bar_code.csv')
###########
###################
'''
#read csv file & write data in QR code
# Creating an instance of QRCode class
read_data=pd.read_csv('Data_Folder/product_data.csv')
count=1
for a,b,c in zip(read_data['Brand'],read_data['Quantity'],read_data['Amount']):
	qr = qrcode.QRCode(version=1,
					   box_size=10,
					   border=5)
	qr.add_data(f"Brand:{a}")
	qr.add_data(f";Quantity:{b}")
	qr.add_data(f";Amount:{c}")
	qr.make(fit=True)
	img = qr.make_image(fill_color='black',
						back_color='white')
	file_name="QR_code"+str(count)+'.png'
	img.save(f"./QR_CODE/{file_name}")
	count+=1
#resize qr-image
import os
from PIL import Image
for x in os.listdir('./QR_CODE/'):
	img_file=Image.open(f'./QR_CODE/{x}')
	img_file=img_file.resize((100,100))
	img_file.save(f"./QR_CODE/{x}")
###################
###############
'''
'''
img_01 = Image.open("./QR_CODE/Box_QR_code1.png")
img_02 = Image.open("./QR_CODE/Box_QR_code2.png")
img_03 = Image.open("./QR_CODE/QR_code3.png")
img_04 = Image.open("./QR_CODE/QR_code4.png")

img_01_size = img_01.size
print('img 1 size: ', img_01_size)

new_im = Image.new('RGB', (2*img_01_size[0],2*img_01_size[1]), (250,250,250))

new_im.paste(img_01, (0,0))
new_im.paste(img_02, (img_01_size[0],0))
new_im.paste(img_03, (0,img_01_size[1]))
new_im.paste(img_04, (img_01_size[0],img_01_size[1]))

new_im.save("merged_images.png", "PNG")
'''
'''
from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol
decoded = decode(Image.open("./QR_CODE/merge_s.png"), symbols=[ZBarSymbol.QRCODE])
print(decoded)
'''
'''
def decoder(image):
    list_of_all_barcode=[]
    barcode = decode(image)
    for x in barcode:
        barcodeData = x.data.decode("utf-8")
        list_of_all_barcode.append(str(barcodeData))
    return list_of_all_barcode
image = Image.open("")
barcodes_list=list(decoder(image))[::-1]
print(f"All bar codes are : {barcodes_list}")
'''
####################
'''
# Data to encode
data = "Brand Name:Signature"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
				box_size = 10,
				border = 5)

# Adding data to the instance 'qr'
qr.add_data(data)
qr.add_data(";Size:750")
qr.add_data(";Pack Size:12")
qr.add_data(";Quantity:600")
qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
					back_color = 'white')

img.save('MyQRCode2.png')
'''
#####################
#Image resize
import numpy as np
from PIL import Image
data=Image.open('./QR_CODE/temp5.png')
data=data.resize((100,100))
data.save('./QR_CODE/temp5.png')

'''
for i in range(4,6):
	qr = qrcode.QRCode(version=1,
					   box_size=10,
					   border=5)
	qr.add_data(i)
	qr.make(fit=True)
	img = qr.make_image(fill_color='black',
						back_color='white')
	file_name="temp"+str(i)+'.png'
	img.save(f"./QR_CODE/{file_name}")
	'''