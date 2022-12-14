# DE MODIFICAT PT A MUTA ANUMITE FILE IN FOLDERE DIFERITE

from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os       
import json



class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(Hub):
            if filename.endswith('2019.docx') : # MODIIFCA PT CE FORMAT VREI
                src = Hub + "/" + filename
                new_destination = Word + '/' + filename
                os.rename(src, new_destination)
            if filename.endswith('.pub') : # MODIIFCA PT CE FORMAT VREI
                src = Hub + "/" + filename
                new_destination = Publisher + '/' + filename
                os.rename(src, new_destination)
            if filename.endswith('.accdb') : # MODIIFCA PT CE FORMAT VREI
                src = Hub + "/" + filename
                new_destination = Acces + '/' + filename
                os.rename(src, new_destination)
            if filename.endswith('.xlsx') : # MODIIFCA PT CE FORMAT VREI
                src = Hub + "/" + filename
                new_destination = Excel + '/' + filename
                os.rename(src, new_destination)
            if filename.endswith('.pptx') : # MODIIFCA PT CE FORMAT VREI
                src = Hub + "/" + filename
                new_destination = Powerpoint + '/' + filename
                os.rename(src, new_destination)




Hub = 'C:\\Users\\Andrei\\Desktop\\Hub'
Word = 'C:\\Users\\Andrei\\Desktop\\Word'
Excel = 'C:\\Users\\Andrei\\Desktop\\Excel'
Powerpoint = 'C:\\Users\\Andrei\\Desktop\\Powerpoint'
Publisher = 'C:\\Users\\Andrei\\Desktop\\Publisher'
Acces = 'C:\\Users\\Andrei\\Desktop\\Acces'
Others = 'C:\\Users\\Andrei\\Desktop\\Others'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, Hub, recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()