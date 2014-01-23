#!/bin/python
import os
import tarfile
import zipfile
import glob
import sys
zipped_files = {}
def extract_file(path, to_directory="."):
    if path.endswith('.zip'):
        opener, mode = zipfile.ZipFile, 'r'
    elif path.endswith('.tar.gz') or path.endswith('.tgz'):
        opener, mode = tarfile.open, 'r:gz'
    elif path.endswith('.tar.bz2') or path.endswith('.tbz'):
        opener, mode = tarfile.open, 'r:bz2'
    else: 
        raise ValueError, "Could not extract `%s` as no appropriate extractor is found" % path
    
    cwd = os.getcwd()
    os.chdir(to_directory)
    
    try:
        file = opener(path, mode)
        try: file.extractall(os.path.expanduser("~/"+sys.argv[1]))
        finally: file.close()
    finally:
        os.chdir(cwd)
count = 0
os.system('clear')
print "Place your source zip/tar file in the input folder of your tool"
raw_input("Press Enter to continue...")
os.chdir(os.path.expanduser("~/dark_multitool1.0/input"))
print "Following files found..."
for files in os.listdir("."):
    if files.endswith('.tar.gz') or files.endswith('.zip') or files.endswith('.tar.bz2'):
        count=count+1
        print ("%s-%s")%(count,files)
        zipped_files.update({count:files})      
x = input("Enter which file you want to extract : ")
os.chdir(os.path.expanduser("~/dark_multitool1.0/input"))
extract_file(zipped_files[x])













