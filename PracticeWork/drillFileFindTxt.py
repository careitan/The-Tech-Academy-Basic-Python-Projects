from os import listdir
from os.path import isfile, join, getmtime
import time

def getTxtFiles():
    searchDir = 'C:\\A\\'
    for file in listdir(searchDir):
        if isfile(join(searchDir,file)):
            # get the file modification time and format it for use.
            modTimeLocal = time.localtime(getmtime(join(searchDir,file)))

            renderFilelistingFormatted(join(searchDir, file), modTimeLocal)

# The following function requires preformstting the ttime value to local time.
# Functionnbelow will only perform the strftime() function to arrange the date string.
def renderFilelistingFormatted(fname, ttime):
    if (fname.find(".txt", len(fname)-5) > -1):
        print("{}\t{}".format(fname, time.strftime('%m/%d/%Y', ttime)))

if __name__ == "__main__":
    getTxtFiles()
