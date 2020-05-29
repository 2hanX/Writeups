# fork from https://github.com/codemicro/ctf-writeups/blob/master/tj2020/zippedup/Unzip.py

from zipfile import ZipFile
import tarfile
import os

folder = 0

maindir = "C:/tjctf/zippedup/"

while True:
    os.chdir("C:/tjctf/zippedup/" + str(folder))
    things = os.listdir()
    for i in things:
        if i.endswith(".zip"):
            with ZipFile(i, 'r') as zipObj:
                zipObj.extractall(maindir)
        elif i.endswith(".bz2"):
            my_tar = tarfile.open(i)
            my_tar.extractall(maindir)
            my_tar.close()
        elif i.endswith(".kz3"):
            with ZipFile(i, 'r') as zipObj:
                zipObj.extractall(maindir)
        elif i.endswith(".gz"):
            my_tar = tarfile.open(i)
            my_tar.extractall(maindir)
            my_tar.close()
        else:
            continue
    os.chdir("..")
    folder += 1
