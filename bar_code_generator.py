import barcode
from barcode.writer import ImageWriter
for x in range(1,100000000001):
    temp_str=str(x)
    final_str='0'*(12-len(temp_str))+temp_str  #I have taken bar code lenght size 12
    hr=barcode.get_barcode_class("code128")
    Hr=hr(final_str,writer=ImageWriter())
    qr=Hr.save("barcode_"+final_str)
    if x==5: # to generate only 5 barcodes
        break

#above code is to generate only 5 barcodes we can extend this as you want
