import os
import urllib.request#для поточных задач
from threading import Thread
from time import time
 
class DownloadThread(Thread):
    """
    многопоточноя загрузка файлов из интернета
    """
    
    def __init__(self, url, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name
        self.url = url
    
    def run(self):
        """Запуск потока"""
        handle = urllib.request.urlopen(self.url)#запускать открытие pdf файла
        fname = os.path.basename(self.url)#будет переиминовывать файл
        
        with open(fname, "wb") as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        
        msg = "%s закончил загрузку %s!" % (self.name, self.url)
        print(msg)
        x1 = time()
        print(x1)

 
 
def main(urls):
    """
    Run the program
    """
    for item, url in enumerate(urls):
        name = "Поток %s" % (item+1)
        thread = DownloadThread(url, name)
        thread.start()
 
if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
    
    main(urls)