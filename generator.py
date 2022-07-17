import qrcode
from PIL import Image
import os


ctr=0
counter=0

file_to_read=open('output.txt', 'r')




currentLink=''
currentModel=''

for line in file_to_read:
    if not counter % 2:
        currentModel=line.strip()
    else:
        currentLink=line.strip()
        
        data=currentLink

        img=qrcode.make(data)

        string_save='model_' + str(ctr) + '.png'

        path_to_save=('./static')



        img=img.save(f"static/QRCodes/{string_save}")
        ctr+=1

    counter+=1   