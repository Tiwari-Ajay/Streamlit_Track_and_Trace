import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image
import barcode
from barcode.writer import ImageWriter
from pyzbar.pyzbar import decode,ZBarSymbol
import qrcode
import cv2
import numpy as np
from pathlib import Path
import os


####################################################
# Complete system flow
################################################
def project_decription():
    title_templ = """
        <h3 style="color:blue"><b>Project Description:</b></h3>
        """
    st.markdown(title_templ, unsafe_allow_html=True)
    data = f"""
                    **Project Name**: Product Tracking Automation System

                    **Domain Name**: Business
                    
                    Focus of the project is to demonstrate the Product Tracking Automation System flow.
                    """
    st.write(data)
def scanning_products_barcode():
    st.write("We can take Image using Camera")
    st.write("For this time I'm going to use Image:")
    uploaded_file = st.file_uploader("Choose Image")
    if uploaded_file:
        file_path="./BAR_CODE/"+uploaded_file.name
        list_of_all_barcode = []
        image = Image.open(file_path)
        st.image(image)
        barcode = decode(image)
        for x in barcode:
            barcodeData = x.data.decode("utf-8")
            list_of_all_barcode.append(str(barcodeData))
        return list_of_all_barcode
def scanning_products_QRcode():

    st.write("We can use Camera")
    st.write("For this time I'm going to use Image:")
    uploaded_file = st.file_uploader("Choose Product QR code Image to Scan")
    list_of_all_barcode = []
    st.write("Single Product QR Image:")
    if uploaded_file:
        file_path="./QR_CODE/"+uploaded_file.name
        st.image(file_path,caption="QR_code_Image")

        image = Image.open(file_path)
        barcode = decode(image)
        for x in barcode:
            barcodeData = x.data.decode("utf-8")
            list_of_all_barcode.append(str(barcodeData))
    list1=[]
    for x in list_of_all_barcode[::-1]:
        list1.append((x))
    # st.write(f"All Product Ids : {list1}")
    if (len(list1)>0):
        st.write("Product Id : ")
        st.success(list1[0])
        #data = pd.Series(list_of_all_barcode, name="QR_Code_Values")
        #data.to_csv('./Data_Folder/temp_QRCode.csv', index=False)
        #st.write(data)
def scanning_box_QRcode():

    st.write("We can use Camera")
    st.write("For this time I'm going to use Image:")
    uploaded_file = st.file_uploader("Choose Box QR code Image to Scan")
    list_of_all_barcode = []
    st.write("Box QR code Information:")
    if uploaded_file:
        file_path="./QR_CODE/"+uploaded_file.name
        st.image(file_path,caption="QR_code_Image")

        image = Image.open(file_path)
        barcode = decode(image)
        for x in barcode:
            barcodeData = x.data.decode("utf-8")
            list_of_all_barcode.append(str(barcodeData))
    list1=[]
    for x in list_of_all_barcode[::-1]:
        list1.append((x))
    # st.write(f"All Product Ids : {list1}")
    path = Path('./temp_data.txt')
    if path.is_file():
        os.remove('./temp_data.txt')
    if (len(list1)>0):
        st.info(f"**Scanned Information : {list1[0]}**")
        st.write(f"**Box Id : {list1[0].split(',')[0]},  Product Ids: {list1[0].split(',')[1]}**")
        with open('temp_data.txt','a+') as f:
            f.write(list1[0].split(',')[1]+'\n')

        #data = pd.Series(list_of_all_barcode, name="QR_Code_Values")
        #data.to_csv('./Data_Folder/temp_QRCode.csv', index=False)
        #st.write(data)

def scanning_products_layer_QRcode():

    st.write("We can use Camera")
    st.write("For this time I'm going to use Image:")
    uploaded_file = st.file_uploader("Choose Product layer QR code Image to Scan")
    list_of_all_barcode = []
    st.write("Product Layer QR Image:")
    if uploaded_file:
        file_path="./QR_CODE/"+uploaded_file.name
        st.image(file_path,caption="QR_code_Image")

        image = Image.open(file_path)
        barcode = decode(image)
        for x in barcode:
            barcodeData = x.data.decode("utf-8")
            list_of_all_barcode.append(str(barcodeData))
    list1=[]
    for x in list_of_all_barcode[::-1]:
        list1.append((x))
    # st.write(f"All Product Ids : {list1}")
    if (len(list1)>0):
        list2=[]
        for x in list1:
            list2.append(int(x))
        st.write("Product Id : ")
        st.success(list2)
        with open('temp_data.txt','a+') as f:
            f.write(str(list2)+'\n')
        #data = pd.Series(list_of_all_barcode, name="QR_Code_Values")
        #data.to_csv('./Data_Folder/temp_QRCode.csv', index=False)
        #st.write(data)
def decode_QR(image):
    decoded = decode(image)
    data = str(decoded[0].data).lstrip('b')
    brand = []
    quantity = []
    amount = []
    id=[]
    for x in data.split(',')[:-1]:
        data1 = [p.split(":")[-1] for p in x.split(';')]
        brand.append(data1[0])
        quantity.append(data1[1])
        amount.append(data1[2])
        id.append(data1[3])
    data = pd.concat(
        [pd.Series(brand, name="Brnd"), pd.Series(quantity, name="Qty"), pd.Series(amount, name="Amt"),pd.Series(id, name="Id")],
        axis=1)
    #st.dataframe(data)
    data.to_csv('./Data_Folder/final_scanned_QR_info.csv',index=False)
def decoder(image):
    list_of_all_barcode=[]
    barcode = decode(image)
    for x in barcode:
        barcodeData = x.data.decode("utf-8")
        list_of_all_barcode.append(str(barcodeData))
    return list_of_all_barcode

def bottle_Detector_and_Counter(image_path):
    st.write("This is uploaded Image")
    image1=Image.open(image_path)
    st.image(image1)
    image=cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    st.write("This is gray scale Image")
    st.image(gray)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = []
    threshold_area = 50
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > threshold_area:  # Set an appropriate threshold area
            filtered_contours.append(contour)
    result_mask = np.zeros_like(thresh)
    cv2.drawContours(result_mask, filtered_contours, -1, 255, thickness=cv2.FILLED)
    result = cv2.bitwise_and(image, image, mask=result_mask)
    #cv2.imshow('Result', result)
    st.write("This is Object Detected Image")
    st.image(result)
    #print('No. of Bottles:', len(filtered_contours))
    #cv2.waitKey(0)
    cv2.destroyAllWindows()
    return len(filtered_contours)
def main():
    title_templ = """
    <div style="background-color:#000080;padding:8px;">
    <h3 style="color:white;padding:15px;text-align:center">Server Application</h3></div>
    """
    st.markdown(title_templ, unsafe_allow_html=True)
    with st.sidebar:
        selected = option_menu(
            menu_title="Project Menu",
            options=["About the Project","Use of Bar Code","Object Detector & Counter","Use of QR Code"],
            default_index=0
        )
    if selected == "About the Project":
        project_decription()
    elif selected == "Use of Bar Code":
        option_list1=["Generate Bar Code","Clicking image of Products BarCode inside Cases","Decode Taken Image Information",
                      "Encode Information of Products using QRCode","Scan QRCode on Cases","Store Information in System" ]
        option1 = st.sidebar.selectbox('Select Operation', option_list1)
        if option1=="Generate Bar Code":
            uploaded_file = st.file_uploader("Choose data file")
            if uploaded_file:
                name=uploaded_file.name
                com_path="./Data_Folder/"+name
                data=pd.read_csv(com_path)
                data.drop('Unnamed: 0', axis=1, inplace=True)
                st.dataframe(data)
                list1=[]
                for x in range(1, 100000000001):
                    temp_str = str(x)
                    final_str = 'B'+'0' * (11 - len(temp_str)) + temp_str  # I have taken bar code lenght size 12
                    hr = barcode.get_barcode_class("code128")
                    Hr = hr(final_str, writer=ImageWriter())
                    qr = Hr.save("./BAR_CODE/"+"barcode_" + final_str)
                    list1.append(final_str)
                    if x == len(data):  # to generate barcodes
                        break
                data['Bar_Code']=pd.Series(list1,name='Bar_Code')
                data.to_csv(com_path)
        elif option1=="Clicking image of Products BarCode inside Cases":
            data=scanning_products_barcode()
            data = pd.Series(data, name="Bar_Code").sort_values()
            data.to_csv('./Data_Folder/temp_barcode.csv',index=False)
        elif option1=="Decode Taken Image Information":
            data=pd.read_csv('./Data_Folder/temp_barcode.csv')
            st.write(data[::])
        elif option1=="Encode Information of Products using QRCode":
            data = pd.read_csv('./Data_Folder/temp_barcode.csv')
            data=data[::]
            qr = qrcode.QRCode(version=1,
                               box_size=10,
                               border=5)
            for a in data['Bar_Code']:
                qr.add_data(f"{a};")
            qr.make(fit=True)
            img = qr.make_image(fill_color='black',back_color='white')
            img=img.resize((100,100))
            file_name = "QR_code_for_Bar" +'.png'
            img.save(f"./BAR_CODE/{file_name}")
            st.write("This is Output QR Code")
            st.image(f"./BAR_CODE/{file_name}")
        elif option1=="Scan QRCode on Cases":
            decoded = decoder(Image.open("./BAR_CODE/QR_code_for_Bar.png"))[0]
            decoded_data=decoded.split(';')[:-1]
            st.dataframe(pd.Series(decoded_data, name="Scanned QRCode Value on Cases"))
            st.success("Scanning Completed")
        elif option1=="Store Information in System":
            st.write("We need to do mapping Bar code to data")
            data=pd.read_csv("./Data_Folder/product_data_Bar_code.csv")
            decoded = decoder(Image.open("./BAR_CODE/QR_code_for_Bar.png"))[0]
            decoded_data = decoded.split(';')[:-1]
            decoded_data=decoded_data.copy()
            #data['Bar_Code_for_Product']=pd.Series(decoded_data,name='Bar_code_Id')
            list2=[]
            p=list(data.loc[:,'Bar_Code']).copy()
            for x in p:
                if x in decoded_data:
                    list2.append("Not Available")
                else:
                    list2.append("Available")
            data['Status'] = pd.Series(list2, name='Status')
            data.drop('Unnamed: 0',axis=1, inplace=True)
            st.dataframe(data)
            data.to_csv("./Data_Folder/product_data_Bar_code.csv")
            print(list2)

    elif selected == "Use of QR Code":
        option_list2 = ["Generate QRCode","Clicking image of Products QRCode inside Cases","Stored Information after Matched",
                      "Encode Information of Products using QRCode","Scan QRCode on Cases","Current Status After Transfer","Scanning QR code for product","scanning box QR code","Scan products layer by layer","Match with Box product id Range"]
        option2 = st.sidebar.selectbox('Select Operation', option_list2)
        if option2=="Generate QRCode":
            uploaded_file = st.file_uploader("Choose data file")
            if uploaded_file:
                name=uploaded_file.name
                com_path="./Data_Folder/"+name
                read_data=pd.read_csv(com_path)
                read_data.drop('Unnamed: 0', axis=1, inplace=True)
                st.dataframe(read_data)
                count=len(read_data)
                '''
                for a, b, c in zip(read_data['Brnd'], read_data['Qty'], read_data['Amt']):
                    qr = qrcode.QRCode(version=1,
                                       box_size=10,
                                       border=5)
                    qr.add_data(f"Brnd:{a}")
                    qr.add_data(f";Qty:{b}")
                    qr.add_data(f";Amt:{c}")
                    qr.add_data(f";Id:{count}")'''
                for a,b in zip(read_data['Box Id'],read_data['Product Id']):
                    qr = qrcode.QRCode(version=1,
                                       box_size=10,
                                       border=5)
                    qr.add_data(a)
                    qr.add_data(',')
                    qr.add_data(b)
                    qr.make(fit=True)
                    img = qr.make_image(fill_color='black',
                                        back_color='white')

                    img=img.resize((100,100))
                    file_name = "QR_code" + str(count) + '.png'
                    img.save(f"./QR_CODE/{file_name}")
                    count -= 1

        elif option2=="Clicking image of Products QRCode inside Cases":
            scanning_products_QRcode()
        elif option2=="Stored Information after Matched":
            data=pd.read_csv('./Data_Folder/temp_QRCode.csv')
            brand = []
            quantity = []
            amount = []
            id=[]
            for x in data['QR_Code_Values']:
                x = x.split(';')
                brand.append(x[0].split(':')[-1])
                quantity.append(x[1].split(':')[-1])
                amount.append(x[2].split(':')[-1])
                id.append(x[3].split(':')[-1])
            data = pd.concat([pd.Series(brand, name="Brand"), pd.Series(quantity, name="Quantity"),
                             pd.Series(amount, name="Amount"),pd.Series(id, name="Id")], axis=1)
            st.dataframe(data)
        elif option2=="Encode Information of Products using QRCode":
            read_data = pd.read_csv('Data_Folder/temp_QRCode.csv')
            qr = qrcode.QRCode(version=1,
                               box_size=10,
                               border=5)
            for x in read_data['QR_Code_Values']:
                qr.add_data(x)
                qr.add_data(",")
            qr.make(fit=True)
            img = qr.make_image(fill_color='black',back_color='white')
            img=img.resize((100,100))
            file_name = "QR_code_final" + '.png'
            img.save(f"./QR_CODE/{file_name}")
            st.write("final Encoded QR Code:")
            st.image(f"./QR_CODE/{file_name}")
        elif option2=="Scan QRCode on Cases":
            image=Image.open("./QR_CODE/QR_code_final.png")
            decode_QR(image)
            st.success("Scanning Completed")
        elif option2=="Current Status After Transfer":
            #st.write("We need to do mapping Bar code to data")
            data=pd.read_csv('./Data_Folder/final_scanned_QR_info.csv')
            data1=pd.read_csv('./Data_Folder/product_data_QR_code.csv')
            list1=[]
            for x,y,z in zip(list(data['Brnd']),list(data['Qty']),list(data['Amt'])):
                if (x in list(data1["Brnd"])) and (y in list(data1["Qty"])) and (z in list(data1["Amt"])):
                    list1.append("Not Available")
                else:
                    list1.append("Available")
            data['Status']=pd.Series(list1, name='Status')
            st.dataframe(data)
            data.to_csv('./Data_Folder/final_scanned_QR_info.csv', index=False)
        elif option2=="Scanning QR code for product":
            scanning_products_QRcode()
        elif option2=="scanning box QR code":
            scanning_box_QRcode()
        elif option2=="Scan products layer by layer":
            scanning_products_layer_QRcode()
        elif option2=="Match with Box product id Range":
            temp=[]
            with open('temp_data.txt','r') as f:
                temp=f.readlines()
            low_range, high_range=temp[0].strip('\n').split('-')
            scanned_range = temp[1].strip('[]\n').split(',')
            scanned_range =[int(x.strip()) for x in scanned_range]
            flag=0
            for i in range(int(low_range),int(high_range)+1):
                if i not in scanned_range:
                    flag=1
                    st.error("Not Matched")
                    break
            if flag==0:
                st.success("Matched")

    elif selected=="Object Detector & Counter":
        quantity=st.text_input("Quantity of Products in Case:")
        st.write("We can take photo from camera")
        st.write("This Time I'm going to take image from system:")
        uploaded_file = st.file_uploader("Choose Image file")
        if uploaded_file:
            no_of_bottles=bottle_Detector_and_Counter("./Image_Detector_Data/" + uploaded_file.name)
            if no_of_bottles==int(quantity):
                st.write("Status:")
                st.success("Ok")
            else:
                st.write("Status:")
                st.error("unacceptable")



main()
