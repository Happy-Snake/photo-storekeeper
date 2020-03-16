import easygui

################################
####### Открываем файлы ########
################################
fotos = None
while fotos == None:
    fotos = easygui.fileopenbox("Select files", "Select files", multiple=True)

################################
### Создаем новую директорию ###
################################

msg = "Куда ездили?"
title = "Ввод города" #Шапочка.
place = easygui.enterbox(msg, title)

import os

path = fotos[1][0:fotos[1].rfind("\\")+1]
os.mkdir(path + place)

################################
##### Считываем метаданные #####
################################
from PIL import Image, ExifTags
import shutil

list_of_dates = []
for i in range(len(fotos)):
    img = Image.open(fotos[i])
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    time = exif['DateTime'][0:10]
    
    while time.find(':') > 0:
        a = time.find(':')
        time = time[:a] + '.' + time[a+1:]

    if time not in list_of_dates:
        os.mkdir(path + place + "\\" + time)
        list_of_dates.append(time)

    shutil.copy(fotos[i], path + place + "\\" + time)
