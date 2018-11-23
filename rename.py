import os
from PIL import Image
import glob
import shutil
# 目录名称，你要自己修改

_dir = "E:\ZDHT/raw/falseface/"


file_name = os.listdir(_dir)

n = 1
for file in file_name:
        oldname = _dir + file
        newname = _dir + 'F_'+file
        os.rename(oldname, newname)
        n = n + 1
        print(oldname, '--->', newname)
