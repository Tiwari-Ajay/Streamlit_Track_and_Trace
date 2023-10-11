from PIL import Image
import os
# Opens a image in RGB mo

#im = Image.open("./Alia_Bhatt_temp/Alia_Bhatt11.jpg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
i=1
for x in os.listdir('./Vidya_Balan_test/'):
    im = Image.open('./Vidya_Balan_test/'+x)
    width, height = im.size
    left = 5
    top = 0
    right = width-10
    bottom = height / 2
    #img_res = im.crop((left, top, right, bottom))
    #img_res.save("./Vidya_Balan_test/"+str(i)+".jpg")
    im.save("./Vidya_Balan/" + str(i) + ".jpg")
    i+=1
    #print(x)


#img_res = im.crop((left, top, right, bottom))

#img_res.show()