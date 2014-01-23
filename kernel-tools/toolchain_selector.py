#!/bin/python
import os
import subprocess
import re
toolchain={}
toolchain_path={}
count=0
os.chdir(os.path.expanduser("~/android_toolchains"))
os.system('clear')
for dirs in os.listdir("."):
    if not dirs.startswith("."):
        count=count+1
        print ("%s-%s")%(count,dirs)
        toolchain.update({count:dirs})
x=input("Enter your choice or press enter to exit!!!")
if x == '':
    quit()
full_path=os.path.expanduser("~/android_toolchains")
ipath=os.path.join(full_path,toolchain[x],"bin")
os.chdir(ipath)
for files in os.listdir("."):
    if files.startswith("arm-eabi"):
        tpath=os.path.join(ipath,"arm-eabi")
        break
    if files.startswith("arm-linux"):
        tpath=os.path.join(ipath,"arm-linux-androideabi")
        break
print tpath
fpath="export toolchain="+tpath
filename=os.path.expanduser("~/dark_multitool1.0/scripts/config")
outfile=os.path.expanduser("~/dark_multitool1.0/scripts/new_config")
word="toolchain"
with open(filename,'r') as fi,open(outfile,'w') as fo:  
    for line in fi:
        if word not in line:
            fo.write(line)
        if word in line:
            fo.write(fpath)
os.remove(filename)
os.rename(outfile, filename)

    
      
