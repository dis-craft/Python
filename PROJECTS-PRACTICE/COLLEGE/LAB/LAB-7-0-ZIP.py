import os
import zipfile

def backupfolder(foldername):
    folderpath = os.path.abspath(foldername)
    backupfile = foldername + '.zip'
    with zipfile.ZipFile(backupfile, 'w') as zff:
        for root,dirs,files in os.walk(folderpath):
            for file in files:
                filepath = os.path.join(root,join)
                zff.write(filepath)
backupfolder('LAB-7-1-test')