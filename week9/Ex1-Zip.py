import threading
import zipfile

class AsyncZip(threading.Thread):
    def __init__(self,infile,outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.ZipFile(self.outfile,'w',zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of: ',self.infile)

background = AsyncZip('7-Multi-threading/mydata.txt',
                        '7-Multi-threading/myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()
