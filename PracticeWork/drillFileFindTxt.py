from os import listdir
from os.path import isfile, join, getmtime


def getTxtFiles():
    searchDir = 'C:\\A\\'
    for file in listdir(searchDir):
        if isfile(join(searchDir,file)):
            renderFilelisting(join(searchDir, file), getmtime(join(searchDir,file)))

def renderFilelisting(fname, ttime):
    print("{}\t{}".format(fname, ttime))


if __name__ == "__main__":
    getTxtFiles()
