import os
import shutil
source=input("enter the source folder name")
destination=input("enter the destination folder name")
source=source+"/"
destination=destination+"/"
listoffile=os.listdir(source)
for file in listoffile: 
    shutil.copy((source+file),destination)

    