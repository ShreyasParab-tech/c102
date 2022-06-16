from os import access
from tracemalloc import take_snapshot
import cv2
import dropbox
import time
import random


def snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(img_name):
    access_token = "sl.BJeEGZfJv8un9UoxkxvPRireGrDoFxwMvtiev9c7SIBuge_9UC32vPTYA6e5t7fDfBiZfX5tDazjilkOmTGpYLPiXIrvOm051OujLLTxB9TenMbXcDwKNJL-ZaPylkV9eiEggYQ"
    file = img_name
    file_from = file
    file_to = "/newfolder/"+(img_name)

    dbx = dropbox.Dropbox(access_token)
        with_open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
            print("File Uploaded")
    

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name = take_snapshot()
            uploadFile(name)

main()
